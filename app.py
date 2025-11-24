from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

app = Flask(__name__)
app.secret_key = "secret_key_for_session" # 用於 Flash 訊息

# 設定資料庫連線
# 格式: mysql+pymysql://帳號:密碼@主機位置/資料庫名稱
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Jeremy&930915@localhost/hrap'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# --- 資料庫模型 (Models) 對應你的 SQL 結構 ---

class Department(db.Model):
    __tablename__ = 'Department'
    DepartmentID = db.Column(db.String(4), primary_key=True)
    DepartmentName = db.Column(db.String(100), nullable=False)
    CostCenter = db.Column(db.String(8), nullable=False)

class Status(db.Model):
    __tablename__ = 'Status'
    StatusID = db.Column(db.String(4), primary_key=True)
    StatusName = db.Column(db.String(50), nullable=False)
    Description = db.Column(db.Text)

class Employee(db.Model):
    __tablename__ = 'Employee'
    EmployeeID = db.Column(db.String(10), primary_key=True)
    FirstName = db.Column(db.String(50), nullable=False)
    LastName = db.Column(db.String(50), nullable=False)
    DateOfBirth = db.Column(db.Date, nullable=False)
    Gender = db.Column(db.Enum('Male', 'Female', 'Other'), nullable=False)
    HireDate = db.Column(db.Date, nullable=False)
    JoinDate = db.Column(db.Date, nullable=False)
    DepartmentID = db.Column(db.String(4), db.ForeignKey('Department.DepartmentID'))
    JobTitle = db.Column(db.String(100), nullable=False)
    CompEmail = db.Column(db.String(100), unique=True, nullable=False)
    PrivateEmail = db.Column(db.String(100))
    PhoneNumber = db.Column(db.String(20))
    Address = db.Column(db.Text)
    StatusID = db.Column(db.String(4), db.ForeignKey('Status.StatusID'))
    
    # 建立關聯以便查詢顯示名稱
    department = db.relationship('Department', backref='employees')
    status = db.relationship('Status', backref='employees')
    salary = db.relationship('Salary', backref='employee', uselist=False, cascade="all, delete-orphan")

class Salary(db.Model):
    __tablename__ = 'Salary'
    SalaryID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    EmployeeID = db.Column(db.String(10), db.ForeignKey('Employee.EmployeeID'), nullable=False)
    DepartmentID = db.Column(db.String(4), db.ForeignKey('Department.DepartmentID'), nullable=False)
    BaseSalary = db.Column(db.Numeric(10, 2), nullable=False)
    Bonus = db.Column(db.Numeric(10, 2), default=0.00)

# --- 路由 (Routes) ---

@app.route('/')
def index():
    # 搜尋功能
    search_query = request.args.get('q')
    if search_query:
        # 搜尋名字、Email 或 ID
        employees = Employee.query.filter(
            (Employee.FirstName.contains(search_query)) | 
            (Employee.LastName.contains(search_query)) |
            (Employee.CompEmail.contains(search_query)) |
            (Employee.EmployeeID.contains(search_query))
        ).all()
    else:
        employees = Employee.query.all()
    
    return render_template('index.html', employees=employees, search_query=search_query)

@app.route('/add', methods=['GET', 'POST'])
def add_employee():
    if request.method == 'POST':
        try:
            # 獲取表單資料
            emp_id = request.form['EmployeeID']
            dept_id = request.form['DepartmentID']
            
            new_emp = Employee(
                EmployeeID=emp_id,
                FirstName=request.form['FirstName'],
                LastName=request.form['LastName'],
                DateOfBirth=request.form['DateOfBirth'],
                Gender=request.form['Gender'],
                HireDate=request.form['HireDate'],
                JoinDate=request.form['JoinDate'],
                DepartmentID=dept_id,
                JobTitle=request.form['JobTitle'],
                CompEmail=request.form['CompEmail'],
                PrivateEmail=request.form['PrivateEmail'],
                PhoneNumber=request.form['PhoneNumber'],
                Address=request.form['Address'],
                StatusID=request.form['StatusID']
            )
            
            # 同時新增薪資資料
            base_salary = request.form.get('BaseSalary', 0)
            bonus = request.form.get('Bonus', 0)
            
            new_salary = Salary(
                EmployeeID=emp_id,
                DepartmentID=dept_id, # Salary 表格也有 DepartmentID
                BaseSalary=base_salary,
                Bonus=bonus
            )
            
            db.session.add(new_emp)
            db.session.add(new_salary)
            db.session.commit()
            flash('員工新增成功！', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            db.session.rollback()
            flash(f'新增失敗: {str(e)}', 'danger')

    departments = Department.query.all()
    statuses = Status.query.all()
    return render_template('employee_form.html', departments=departments, statuses=statuses, employee=None)

@app.route('/edit/<string:id>', methods=['GET', 'POST'])
def edit_employee(id):
    employee = Employee.query.get_or_404(id)
    salary = Salary.query.filter_by(EmployeeID=id).first()
    
    if request.method == 'POST':
        try:
            employee.FirstName = request.form['FirstName']
            employee.LastName = request.form['LastName']
            employee.DepartmentID = request.form['DepartmentID']
            employee.JobTitle = request.form['JobTitle']
            employee.StatusID = request.form['StatusID']
            employee.PhoneNumber = request.form['PhoneNumber']
            employee.CompEmail = request.form['CompEmail']
            
            # 更新薪資
            if salary:
                salary.BaseSalary = request.form['BaseSalary']
                salary.Bonus = request.form['Bonus']
                salary.DepartmentID = request.form['DepartmentID'] # 更新部門時同步更新薪資表的部門
            else:
                # 如果原本沒有薪資資料，則新增
                new_salary = Salary(
                    EmployeeID=id,
                    DepartmentID=request.form['DepartmentID'],
                    BaseSalary=request.form['BaseSalary'],
                    Bonus=request.form['Bonus']
                )
                db.session.add(new_salary)

            db.session.commit()
            flash('員工資料更新成功！', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            db.session.rollback()
            flash(f'更新失敗: {str(e)}', 'danger')

    departments = Department.query.all()
    statuses = Status.query.all()
    return render_template('employee_form.html', departments=departments, statuses=statuses, employee=employee, salary=salary)

@app.route('/delete/<string:id>', methods=['POST'])
def delete_employee(id):
    try:
        employee = Employee.query.get_or_404(id)
        # 因為 Salary 設定了 cascade，刪除 Employee 會自動處理 (或手動刪除)
        db.session.delete(employee)
        db.session.commit()
        flash('員工已刪除', 'warning')
    except Exception as e:
        db.session.rollback()
        flash(f'刪除失敗: {str(e)}', 'danger')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)