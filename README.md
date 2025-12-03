# HRAP - HRIS Analysis Platform

## 🚀 Project Overview
**HRAP (Human Resource Analysis Platform)** is a comprehensive web-based application designed to modernize HR data management and decision-making. By integrating **Machine Learning (Random Forest)** with traditional **HRIS functionalities**, HRAP goes beyond simple data storage to provide actionable insights into employee turnover risk and salary alignment.

📺 **Proposal Video:** [Watch on YouTube](https://youtu.be/NAzth4Bz-Ag)

---

## 🔍 Key Features

### 1. **Core HRIS (CRUD System)**
- **Create**: Onboard new employees with ease.
- **Read**: View detailed employee profiles and salary information.
- **Update**: Modify employee records and salary details.
- **Delete**: Remove inactive employee records.
- **Search**: Quickly find employees by Name or ID.

### 2. **Advanced Analytics Dashboard**
- **Automated Clustering**: Uses **PCA** and **K-Means** to group employees into distinct personas (e.g., Junior Associates, Senior Leaders) based on tenure and salary.
- **Visual Insights**: Interactive charts and summaries to understand workforce composition.

### 3. **Predictive Machine Learning** 🤖
- **Turnover Risk Prediction**:
  - Uses a **Random Forest Classifier** to estimate the probability of an employee leaving.
  - Classifies employees into **High**, **Medium**, and **Low** risk categories.
  - **New**: "Risk Probability" now specifically indicates the likelihood of being **High Risk**, providing a clear warning signal.
- **Salary Alignment Analysis**:
  - Uses a **Random Forest Regressor** to predict market-value salaries based on role, experience, and department.
  - Identifies employees who are **Underpaid (Below Market)**, **Overpaid (Above Market)**, or **Market Aligned**.

### 4. **Actionable Reporting**
- **Detailed Classification Lists**: Expandable lists to view specific employees in each risk or salary category.
- **CSV Export**: One-click export of the complete analysis, including ML predictions, for further offline processing.

---

## 🛠️ Technology Stack

- **Frontend**: HTML5, CSS3, Bootstrap 5, Jinja2 Templates
- **Backend**: Python, Flask
- **Database**: MySQL (SQLAlchemy ORM)
- **Machine Learning**: Scikit-learn (Random Forest, PCA, K-Means), Pandas
- **Tools**: Git, Visual Studio Code

---

## ⚙️ Installation & Setup

### 1. Prerequisites
- Python 3.8+
- MySQL Server

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Database Configuration
Create a `config.py` file in the root directory:
```python
DB_HOST = "localhost"
DB_USER = "your_username"
DB_PASSWORD = "your_password"
DB_NAME = "HRAP_DB"
```

### 4. Train Models
Before running the analysis, ensure the ML models are trained:
```bash
python train_models.py
```

### 5. Run the Application
```bash
python app.py
```
Visit `http://127.0.0.1:5000` in your browser.

---

## 🗂 ER Diagram

Below is the Entity-Relationship Diagram for our HRAP system:

<img width="1920" height="1080" alt="HRAP HRIS Analysis Platform (1)" src="https://github.com/user-attachments/assets/0600a00c-1106-4646-b023-6e6567eee47f" />

---

## 👥 Team & Responsibilities

| Member | Responsibilities |
|--------|------------------|
| **洪明凱** | Update, Delete Functions |
| **高郁城** | Create, Read Functions |
| **李東璟** | Search Functionality |
| **All Members** | Data Analysis Dashboard & ML Integration |

---

## 📅 Development Timeline

| Week | Task |
|------|------|
| **W12** | Core CRUD (Create, Read) |
| **W13** | Core CRUD (Update, Delete) |
| **W14** | Search Implementation |
| **W15** | Data Analysis & ML Integration |
| **W16** | Final Polish & Video Submission |
