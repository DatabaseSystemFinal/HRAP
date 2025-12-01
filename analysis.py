import pandas as pd
from sqlalchemy import create_engine
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from datetime import datetime
import config

# 1. Database Connection Configuration
# Replace with your actual username, password, and settings
# Format: mysql+pymysql://username:password@host/db_name
db_connection_str = f'mysql+pymysql://{config.DB_USER}:{config.DB_PASSWORD}@{config.DB_HOST}/{config.DB_NAME}'
db_connection = create_engine(db_connection_str)

def get_analysis_results():
    # 2. SQL Query (The JOIN query we discussed)
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

    # Load directly into Pandas
    df = pd.read_sql(query, db_connection)

    # 3. Preprocessing
    current_year = datetime.now().year
    df['DateOfBirth'] = pd.to_datetime(df['DateOfBirth'])
    df['HireDate'] = pd.to_datetime(df['HireDate'])
    
    # Feature Engineering
    df['Age'] = current_year - df['DateOfBirth'].dt.year
    df['Tenure'] = current_year - df['HireDate'].dt.year
    df['TotalComp'] = df['BaseSalary'] + df['Bonus']

    # Select features for ML
    features = df[['Age', 'Tenure', 'BaseSalary', 'Bonus', 'Gender', 'DepartmentName', 'StatusName']]
    
    # One Hot Encoding
    features_encoded = pd.get_dummies(features, columns=['Gender', 'DepartmentName', 'StatusName'])

    # Scaling
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features_encoded)

    # 4. PCA
    pca = PCA(n_components=0.90) # Keep 90% variance
    pca_data = pca.fit_transform(scaled_features)

    # 5. K-Means
    # Assuming 4 clusters for this example
    kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
    df['Cluster_ID'] = kmeans.fit_predict(pca_data)

    # 1. SORTING: Sort by Cluster_ID (0-3), then by Department
    df = df.sort_values(by=['Cluster_ID', 'DepartmentName'])

    # 2. PREPARE SUMMARY (Keep this as HTML or convert to dict if you prefer)
    summary = df.groupby('Cluster_ID')[['Age', 'Tenure', 'BaseSalary', 'Bonus']].mean().round(1).reset_index()
    counts = df['Cluster_ID'].value_counts().reset_index()
    counts.columns = ['Cluster_ID', 'Count']
    summary = pd.merge(summary, counts, on='Cluster_ID')
    
    # Convert summary to HTML (We can keep this one as is, or style it manually too)
    summary_data = summary.to_dict(orient='records')

    # 3. PREPARE DETAILS: Convert to a list of dictionaries for the template
    # We select the columns we want to display
    details_data = df[['EmployeeID', 'FirstName', 'LastName', 'DepartmentName', 'JobTitle', 'Cluster_ID']].to_dict(orient='records')

    return summary_data, details_data