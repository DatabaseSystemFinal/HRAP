"""
訓練並儲存優化的 Random Forest 模型
針對小數據集優化,使用增強特徵工程
"""
import pandas as pd
import pickle
import os
from sqlalchemy import create_engine
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score, mean_absolute_error, r2_score, classification_report
from datetime import datetime
import config

# 建立 models 目錄
os.makedirs('models', exist_ok=True)

# Database Connection
db_connection_str = f'mysql+pymysql://{config.DB_USER}:{config.DB_PASSWORD}@{config.DB_HOST}/{config.DB_NAME}'
db_connection = create_engine(db_connection_str)

print("📊 載入員工資料...")
query = """
SELECT 
    e.EmployeeID, e.FirstName, e.LastName,
    e.DateOfBirth, e.HireDate, e.Gender, e.JobTitle,
    d.DepartmentName, s.StatusName,
    sa.BaseSalary, sa.Bonus
FROM Employee e
JOIN Salary sa ON e.EmployeeID = sa.EmployeeID
JOIN Department d ON e.DepartmentID = d.DepartmentID
JOIN Status s ON e.StatusID = s.StatusID;
"""

df = pd.read_sql(query, db_connection)
print(f"✅ 載入 {len(df)} 筆員工資料")

# Feature Engineering
current_year = datetime.now().year
df['DateOfBirth'] = pd.to_datetime(df['DateOfBirth'])
df['HireDate'] = pd.to_datetime(df['HireDate'])
df['Age'] = current_year - df['DateOfBirth'].dt.year
df['Tenure'] = current_year - df['HireDate'].dt.year
df['TotalComp'] = df['BaseSalary'] + df['Bonus']

# ============================================
# 1. 訓練離職風險預測模型 (Random Forest)
# ============================================
print("\n🌲 訓練 Random Forest 離職風險預測模型...")

def calculate_turnover_risk(row):
    """Rule-based turnover risk calculation"""
    if row['StatusName'] in ['Temp', 'Ext']:
        return 'High'
    elif row['Tenure'] < 3:
        if row['TotalComp'] < 40000:
            return 'High'
        else:
            return 'Medium'
    elif row['Tenure'] < 7:
        if row['TotalComp'] < df['TotalComp'].median():
            return 'Medium'
        else:
            return 'Low'
    else:
        if row['TotalComp'] >= df['TotalComp'].quantile(0.4):
            return 'Low'
        else:
            return 'Medium'

df['TurnoverRisk_Actual'] = df.apply(calculate_turnover_risk, axis=1)

# 增強特徵工程 (精簡版 - 只保留最重要的特徵)
print("   🔧 進行特徵工程...")
df['Salary_to_Median_Ratio'] = df['BaseSalary'] / df['BaseSalary'].median()
df['Bonus_to_Salary_Ratio'] = df['Bonus'] / (df['BaseSalary'] + 1)
df['Is_Low_Salary'] = (df['BaseSalary'] < df['BaseSalary'].quantile(0.25)).astype(int)
df['Is_New_Employee'] = (df['Tenure'] < 2).astype(int)
df['Is_Senior'] = (df['Tenure'] >= 7).astype(int)
df['Comp_per_Year'] = df['TotalComp'] / (df['Tenure'] + 1)
df['Risk_Score'] = (
    (df['Is_New_Employee'] * 2) +
    (df['Is_Low_Salary'] * 2) +
    ((df['StatusName'].isin(['Temp', 'Ext'])).astype(int) * 3)
)

# Encode categorical variables
le_gender = LabelEncoder()
le_dept = LabelEncoder()
le_status = LabelEncoder()
le_job = LabelEncoder()
le_risk = LabelEncoder()

df['TurnoverRisk_Encoded'] = le_risk.fit_transform(df['TurnoverRisk_Actual'])

# 精簡特徵集 (只用最重要的)
turnover_features = df[['Age', 'Tenure', 'BaseSalary', 'Bonus', 'TotalComp', 
                         'Gender', 'DepartmentName', 'StatusName',
                         'Salary_to_Median_Ratio', 'Is_Low_Salary',
                         'Is_New_Employee', 'Is_Senior',
                         'Comp_per_Year', 'Risk_Score']].copy()

turnover_features['Gender_Encoded'] = le_gender.fit_transform(turnover_features['Gender'])
turnover_features['Department_Encoded'] = le_dept.fit_transform(turnover_features['DepartmentName'])
turnover_features['Status_Encoded'] = le_status.fit_transform(turnover_features['StatusName'])

X_turnover = turnover_features[['Age', 'Tenure', 'BaseSalary', 'Bonus', 'TotalComp',
                                 'Gender_Encoded', 'Department_Encoded', 'Status_Encoded',
                                 'Salary_to_Median_Ratio', 'Is_Low_Salary',
                                 'Is_New_Employee', 'Is_Senior',
                                 'Comp_per_Year', 'Risk_Score']]
y_turnover = df['TurnoverRisk_Actual']  # Random Forest 可以直接用字串標籤

# Split data
X_train_t, X_test_t, y_train_t, y_test_t = train_test_split(
    X_turnover, y_turnover, test_size=0.2, random_state=42, stratify=y_turnover
)

# GridSearchCV 尋找最佳參數 (針對小數據集)
print("   🔍 尋找最佳 Random Forest 參數...")
param_grid = {
    'n_estimators': [100, 150, 200],
    'max_depth': [5, 7, 10, None],
    'min_samples_split': [2, 5],
    'min_samples_leaf': [1, 2],
    'max_features': ['sqrt', 'log2']
}

rf_turnover_base = RandomForestClassifier(
    random_state=42,
    class_weight='balanced',
    bootstrap=True
)

grid_search = GridSearchCV(
    rf_turnover_base, 
    param_grid, 
    cv=3,
    scoring='accuracy',
    n_jobs=-1,
    verbose=0
)

grid_search.fit(X_train_t, y_train_t)
rf_turnover = grid_search.best_estimator_

print(f"   ✅ 最佳參數: {grid_search.best_params_}")
print(f"   📊 交叉驗證分數: {grid_search.best_score_*100:.1f}%")

# Evaluate on test set
y_pred_test = rf_turnover.predict(X_test_t)
turnover_accuracy = accuracy_score(y_test_t, y_pred_test)
print(f"   ✅ 測試集準確率: {turnover_accuracy*100:.1f}%")

# 詳細分類報告
print("\n   📋 分類報告:")
print(classification_report(y_test_t, y_pred_test, zero_division=0))

# 特徵重要性
feature_importance = rf_turnover.feature_importances_
feature_names = X_turnover.columns
top_features = sorted(zip(feature_names, feature_importance), key=lambda x: x[1], reverse=True)[:5]
print(f"   🔝 前5重要特徵:")
for name, imp in top_features:
    print(f"      - {name}: {imp:.3f}")

# ============================================
# 2. 訓練薪資預測模型
# ============================================
print("\n💰 訓練薪資預測模型...")

salary_features = df[['Age', 'Tenure', 'Gender', 'DepartmentName', 'JobTitle']].copy()
salary_features['Gender_Encoded'] = le_gender.transform(salary_features['Gender'])
salary_features['Department_Encoded'] = le_dept.transform(salary_features['DepartmentName'])
salary_features['JobTitle_Encoded'] = le_job.fit_transform(salary_features['JobTitle'])

X_salary = salary_features[['Age', 'Tenure', 'Gender_Encoded', 
                             'Department_Encoded', 'JobTitle_Encoded']]
y_salary = df['BaseSalary']

# Split data
X_train_s, X_test_s, y_train_s, y_test_s = train_test_split(
    X_salary, y_salary, test_size=0.2, random_state=42
)

# Train Random Forest Regressor
rf_salary = RandomForestRegressor(
    n_estimators=150,
    max_depth=10,
    random_state=42,
    min_samples_split=2
)
rf_salary.fit(X_train_s, y_train_s)

# Evaluate
y_pred_test_salary = rf_salary.predict(X_test_s)
salary_mae = mean_absolute_error(y_test_s, y_pred_test_salary)
salary_r2 = r2_score(y_test_s, y_pred_test_salary)
print(f"   ✅ 薪資預測 MAE: ${salary_mae:.2f}")
print(f"   ✅ 薪資預測 R²: {salary_r2:.3f}")

# ============================================
# 3. 儲存模型和編碼器
# ============================================
print("\n💾 儲存模型檔案...")

with open('models/turnover_model.pkl', 'wb') as f:
    pickle.dump(rf_turnover, f)
print("   ✅ 已儲存: models/turnover_model.pkl")

with open('models/salary_model.pkl', 'wb') as f:
    pickle.dump(rf_salary, f)
print("   ✅ 已儲存: models/salary_model.pkl")

encoders = {
    'gender': le_gender,
    'department': le_dept,
    'status': le_status,
    'job': le_job,
    'risk': le_risk
}
with open('models/encoders.pkl', 'wb') as f:
    pickle.dump(encoders, f)
print("   ✅ 已儲存: models/encoders.pkl")

metrics = {
    'turnover_accuracy': round(turnover_accuracy * 100, 1),
    'turnover_cv_score': round(grid_search.best_score_ * 100, 1),
    'salary_mae': round(salary_mae, 2),
    'salary_r2': round(salary_r2, 3),
    'trained_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    'training_samples': len(df),
    'model_type': 'Random Forest (Optimized)',
    'best_params': grid_search.best_params_
}
with open('models/metrics.pkl', 'wb') as f:
    pickle.dump(metrics, f)
print("   ✅ 已儲存: models/metrics.pkl")

print("\n🎉 模型訓練完成!")
print(f"📁 模型檔案已儲存至 models/ 目錄")
print(f"📊 訓練樣本數: {len(df)}")
print(f"🎯 離職風險準確率: {turnover_accuracy*100:.1f}%")
print(f"🌲 模型類型: Random Forest (針對小數據集優化)")
