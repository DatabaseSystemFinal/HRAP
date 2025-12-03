import pandas as pd
import pickle
import os
from sqlalchemy import create_engine
from datetime import datetime
import config

# Database Connection
db_connection_str = f'mysql+pymysql://{config.DB_USER}:{config.DB_PASSWORD}@{config.DB_HOST}/{config.DB_NAME}'
db_connection = create_engine(db_connection_str)

def load_models():
    """載入預訓練的模型和編碼器"""
    models_dir = 'models'
    
    # 檢查模型檔案是否存在
    if not os.path.exists(f'{models_dir}/turnover_model.pkl'):
        raise FileNotFoundError(
            "找不到模型檔案! 請先執行 'python train_models.py' 來訓練模型"
        )
    
    # 載入模型
    with open(f'{models_dir}/turnover_model.pkl', 'rb') as f:
        turnover_model = pickle.load(f)
    
    with open(f'{models_dir}/salary_model.pkl', 'rb') as f:
        salary_model = pickle.load(f)
    
    with open(f'{models_dir}/encoders.pkl', 'rb') as f:
        encoders = pickle.load(f)
    
    with open(f'{models_dir}/metrics.pkl', 'rb') as f:
        metrics = pickle.load(f)
    
    return turnover_model, salary_model, encoders, metrics

def get_prediction_results():
    """
    使用預訓練模型生成員工離職風險和薪資預測
    Returns both summary statistics and detailed predictions for each employee.
    """
    
    # 載入預訓練模型
    turnover_model, salary_model, encoders, saved_metrics = load_models()
    
    # Load employee data
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
    
    # Feature Engineering
    current_year = datetime.now().year
    df['DateOfBirth'] = pd.to_datetime(df['DateOfBirth'])
    df['HireDate'] = pd.to_datetime(df['HireDate'])
    df['Age'] = current_year - df['DateOfBirth'].dt.year
    df['Tenure'] = current_year - df['HireDate'].dt.year
    df['TotalComp'] = df['BaseSalary'] + df['Bonus']
    
    # ============================================
    # 1. 離職風險預測 (使用預訓練模型)
    # ============================================
    
    # 增強特徵工程 (精簡版 - 與訓練時相同)
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
    
    # 準備特徵 (精簡版)
    turnover_features = df[['Age', 'Tenure', 'BaseSalary', 'Bonus', 'TotalComp', 
                             'Gender', 'DepartmentName', 'StatusName',
                             'Salary_to_Median_Ratio', 'Is_Low_Salary',
                             'Is_New_Employee', 'Is_Senior',
                             'Comp_per_Year', 'Risk_Score']].copy()
    
    # 使用儲存的編碼器
    turnover_features['Gender_Encoded'] = encoders['gender'].transform(turnover_features['Gender'])
    turnover_features['Department_Encoded'] = encoders['department'].transform(turnover_features['DepartmentName'])
    turnover_features['Status_Encoded'] = encoders['status'].transform(turnover_features['StatusName'])
    
    X_turnover = turnover_features[['Age', 'Tenure', 'BaseSalary', 'Bonus', 'TotalComp',
                                     'Gender_Encoded', 'Department_Encoded', 'Status_Encoded',
                                     'Salary_to_Median_Ratio', 'Is_Low_Salary',
                                     'Is_New_Employee', 'Is_Senior',
                                     'Comp_per_Year', 'Risk_Score']]
    
    # 使用預訓練模型進行預測 (Random Forest 直接輸出字串標籤)
    df['TurnoverRisk'] = turnover_model.predict(X_turnover)
    
    # 修正: Risk Probability 應該顯示 "High Risk" 的機率,而不是預測類別的信心度
    # 這樣 "Low Risk" 的員工就會有很低的 Risk Probability,符合使用者直覺
    try:
        high_risk_idx = list(turnover_model.classes_).index('High')
        df['TurnoverRisk_Probability'] = turnover_model.predict_proba(X_turnover)[:, high_risk_idx] * 100
    except (ValueError, IndexError):
        # 如果模型中沒有 'High' 類別 (極少見),則設為 0
        df['TurnoverRisk_Probability'] = 0.0
    
    # ============================================
    # 2. 薪資預測 (使用預訓練模型)
    # ============================================
    
    # 準備特徵
    salary_features = df[['Age', 'Tenure', 'Gender', 'DepartmentName', 'JobTitle']].copy()
    salary_features['Gender_Encoded'] = encoders['gender'].transform(salary_features['Gender'])
    salary_features['Department_Encoded'] = encoders['department'].transform(salary_features['DepartmentName'])
    salary_features['JobTitle_Encoded'] = encoders['job'].transform(salary_features['JobTitle'])
    
    X_salary = salary_features[['Age', 'Tenure', 'Gender_Encoded', 
                                 'Department_Encoded', 'JobTitle_Encoded']]
    
    # 使用預訓練模型進行預測
    df['PredictedSalary'] = salary_model.predict(X_salary)
    df['SalaryDifference'] = df['BaseSalary'] - df['PredictedSalary']
    df['SalaryDifference_Pct'] = (df['SalaryDifference'] / df['PredictedSalary'] * 100).round(1)
    
    # 分類薪資對齊狀態
    def categorize_salary_alignment(pct_diff):
        if pct_diff > 10:
            return 'Above Market'
        elif pct_diff < -10:
            return 'Below Market'
        else:
            return 'Market Aligned'
    
    df['SalaryAlignment'] = df['SalaryDifference_Pct'].apply(categorize_salary_alignment)
    
    # ============================================
    # 3. 準備摘要資料
    # ============================================
    
    # 離職風險摘要
    turnover_summary = df['TurnoverRisk'].value_counts().to_dict()
    turnover_summary_list = [
        {'Risk_Level': level, 'Count': count, 'Percentage': round(count/len(df)*100, 1)}
        for level, count in sorted(turnover_summary.items())
    ]
    
    # 薪資對齊摘要
    salary_summary = df['SalaryAlignment'].value_counts().to_dict()
    salary_summary_list = [
        {'Alignment': alignment, 'Count': count, 'Percentage': round(count/len(df)*100, 1)}
        for alignment, count in sorted(salary_summary.items())
    ]
    
    # ============================================
    # 4. 準備詳細資料
    # ============================================
    
    details_data = df[[
        'EmployeeID', 'FirstName', 'LastName', 'DepartmentName', 'JobTitle',
        'Age', 'Tenure', 'BaseSalary', 'TotalComp',
        'TurnoverRisk', 'TurnoverRisk_Probability',
        'PredictedSalary', 'SalaryDifference', 'SalaryDifference_Pct', 'SalaryAlignment'
    ]].copy()
    
    # 依離職風險排序
    risk_order = {'High': 0, 'Medium': 1, 'Low': 2}
    details_data['Risk_Order'] = details_data['TurnoverRisk'].map(risk_order)
    details_data = details_data.sort_values(['Risk_Order', 'SalaryDifference_Pct'])
    details_data = details_data.drop('Risk_Order', axis=1)
    
    details_data_dict = details_data.to_dict(orient='records')
    
    return {
        'turnover_summary': turnover_summary_list,
        'salary_summary': salary_summary_list,
        'model_metrics': saved_metrics,  # 使用訓練時儲存的指標
        'details': details_data_dict
    }

