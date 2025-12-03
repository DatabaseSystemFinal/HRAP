# 在 analysis.html 中插入員工分類詳細列表
import os

template_path = os.path.join(os.path.dirname(__file__), 'templates', 'analysis.html')

with open(template_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 找到插入點 (在預測分析區塊結束後)
marker = '</div>\n\n<!-- Section 3: Detailed List Card -->'

# 準備要插入的員工分類列表 HTML
employee_list_section = '''</div>

<!-- Section 2.5: 員工分類詳細列表 -->
<div class="card shadow-sm mb-4">
    <div class="card-header bg-white py-3">
        <h5 class="mb-0 text-primary">
            <i class="fa-solid fa-users me-2"></i>員工分類詳細列表
        </h5>
    </div>
    <div class="card-body">
        <p class="text-muted mb-4">
            點擊展開查看每個風險等級和薪資對齊類別下的具體員工
        </p>
        
        <!-- 離職風險分類 -->
        <h6 class="fw-bold mb-3">
            <i class="fa-solid fa-exclamation-triangle me-2 text-warning"></i>依離職風險分類
        </h6>
        
        <div class="accordion mb-4" id="turnoverRiskAccordion">
            <!-- High Risk -->
            <div class="accordion-item border-danger">
                <h2 class="accordion-header">
                    <button class="accordion-button collapsed bg-danger bg-opacity-10" type="button" data-bs-toggle="collapse" data-bs-target="#highRisk">
                        <i class="fa-solid fa-circle-xmark text-danger me-2"></i>
                        <strong>高風險 (High Risk)</strong>
                        <span class="badge bg-danger ms-2">
                            {{ prediction_data.details | selectattr('TurnoverRisk', 'equalto', 'High') | list | length }} 人
                        </span>
                    </button>
                </h2>
                <div id="highRisk" class="accordion-collapse collapse" data-bs-parent="#turnoverRiskAccordion">
                    <div class="accordion-body">
                        <div class="table-responsive">
                            <table class="table table-sm table-hover">
                                <thead class="table-light">
                                    <tr>
                                        <th>員工編號</th>
                                        <th>姓名</th>
                                        <th>部門</th>
                                        <th>職位</th>
                                        <th>年資</th>
                                        <th>薪資</th>
                                        <th>風險機率</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    {% for emp in prediction_data.details %}
                                        {% if emp.TurnoverRisk == 'High' %}
                                        <tr>
                                            <td>{{ emp.EmployeeID }}</td>
                                            <td>{{ emp.FirstName }} {{ emp.LastName }}</td>
                                            <td>{{ emp.DepartmentName }}</td>
                                            <td>{{ emp.JobTitle }}</td>
                                            <td>{{ emp.Tenure }} 年</td>
                                            <td>${{ "{:,.0f}".format(emp.BaseSalary) }}</td>
                                            <td><span class="badge bg-danger">{{ "{:.1f}".format(emp.TurnoverRisk_Probability) }}%</span></td>
                                        </tr>
                                        {% endif %}
                                    {% endfor %}
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>
            </div>
            
            <!-- Medium Risk -->
            <div class="accordion-item border-warning">
                <h2 class="accordion-header">
                    <button class="accordion-button collapsed bg-warning bg-opacity-10" type="button" data-bs-toggle="collapse" data-bs-target="#mediumRisk">
                        <i class="fa-solid fa-circle-exclamation text-warning me-2"></i>
                        <strong>中風險 (Medium Risk)</strong>
                        <span class="badge bg-warning ms-2">
                            {{ prediction_data.details | selectattr('TurnoverRisk', 'equalto', 'Medium') | list | length }} 人
                        </span>
                    </button>
                </h2>
                <div id="mediumRisk" class="accordion-collapse collapse" data-bs-parent="#turnoverRiskAccordion">
                    <div class="accordion-body">
                        <div class="table-responsive">
                            <table class="table table-sm table-hover">
                                <thead class="table-light">
                                    <tr>
                                        <th>員工編號</th>
                                        <th>姓名</th>
                                        <th>部門</th>
                                        <th>職位</th>
                                        <th>年資</th>
                                        <th>薪資</th>
                                        <th>風險機率</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    {% for emp in prediction_data.details %}
                                        {% if emp.TurnoverRisk == 'Medium' %}
                                        <tr>
                                            <td>{{ emp.EmployeeID }}</td>
                                            <td>{{ emp.FirstName }} {{ emp.LastName }}</td>
                                            <td>{{ emp.DepartmentName }}</td>
                                            <td>{{ emp.JobTitle }}</td>
                                            <td>{{ emp.Tenure }} 年</td>
                                            <td>${{ "{:,.0f}".format(emp.BaseSalary) }}</td>
                                            <td><span class="badge bg-warning">{{ "{:.1f}".format(emp.TurnoverRisk_Probability) }}%</span></td>
                                        </tr>
                                        {% endif %}
                                    {% endfor %}
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>
            </div>
            
            <!-- Low Risk -->
            <div class="accordion-item border-success">
                <h2 class="accordion-header">
                    <button class="accordion-button collapsed bg-success bg-opacity-10" type="button" data-bs-toggle="collapse" data-bs-target="#lowRisk">
                        <i class="fa-solid fa-circle-check text-success me-2"></i>
                        <strong>低風險 (Low Risk)</strong>
                        <span class="badge bg-success ms-2">
                            {{ prediction_data.details | selectattr('TurnoverRisk', 'equalto', 'Low') | list | length }} 人
                        </span>
                    </button>
                </h2>
                <div id="lowRisk" class="accordion-collapse collapse" data-bs-parent="#turnoverRiskAccordion">
                    <div class="accordion-body">
                        <div class="table-responsive">
                            <table class="table table-sm table-hover">
                                <thead class="table-light">
                                    <tr>
                                        <th>員工編號</th>
                                        <th>姓名</th>
                                        <th>部門</th>
                                        <th>職位</th>
                                        <th>年資</th>
                                        <th>薪資</th>
                                        <th>風險機率</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    {% for emp in prediction_data.details %}
                                        {% if emp.TurnoverRisk == 'Low' %}
                                        <tr>
                                            <td>{{ emp.EmployeeID }}</td>
                                            <td>{{ emp.FirstName }} {{ emp.LastName }}</td>
                                            <td>{{ emp.DepartmentName }}</td>
                                            <td>{{ emp.JobTitle }}</td>
                                            <td>{{ emp.Tenure }} 年</td>
                                            <td>${{ "{:,.0f}".format(emp.BaseSalary) }}</td>
                                            <td><span class="badge bg-success">{{ "{:.1f}".format(emp.TurnoverRisk_Probability) }}%</span></td>
                                        </tr>
                                        {% endif %}
                                    {% endfor %}
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        
        <!-- 薪資對齊分類 -->
        <h6 class="fw-bold mb-3 mt-4">
            <i class="fa-solid fa-dollar-sign me-2 text-success"></i>依薪資對齊分類
        </h6>
        
        <div class="accordion" id="salaryAlignmentAccordion">
            <!-- Below Market -->
            <div class="accordion-item border-danger">
                <h2 class="accordion-header">
                    <button class="accordion-button collapsed bg-danger bg-opacity-10" type="button" data-bs-toggle="collapse" data-bs-target="#belowMarket">
                        <i class="fa-solid fa-arrow-down text-danger me-2"></i>
                        <strong>低於市場 (Below Market)</strong>
                        <span class="badge bg-danger ms-2">
                            {{ prediction_data.details | selectattr('SalaryAlignment', 'equalto', 'Below Market') | list | length }} 人
                        </span>
                    </button>
                </h2>
                <div id="belowMarket" class="accordion-collapse collapse" data-bs-parent="#salaryAlignmentAccordion">
                    <div class="accordion-body">
                        <div class="alert alert-warning border-0">
                            <i class="fa-solid fa-lightbulb me-2"></i>
                            <strong>建議:</strong> 這些員工的薪資低於預測值超過 10%,建議考慮調薪以降低離職風險
                        </div>
                        <div class="table-responsive">
                            <table class="table table-sm table-hover">
                                <thead class="table-light">
                                    <tr>
                                        <th>員工編號</th>
                                        <th>姓名</th>
                                        <th>部門</th>
                                        <th>職位</th>
                                        <th>實際薪資</th>
                                        <th>預測薪資</th>
                                        <th>差異</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    {% for emp in prediction_data.details %}
                                        {% if emp.SalaryAlignment == 'Below Market' %}
                                        <tr>
                                            <td>{{ emp.EmployeeID }}</td>
                                            <td>{{ emp.FirstName }} {{ emp.LastName }}</td>
                                            <td>{{ emp.DepartmentName }}</td>
                                            <td>{{ emp.JobTitle }}</td>
                                            <td>${{ "{:,.0f}".format(emp.BaseSalary) }}</td>
                                            <td>${{ "{:,.0f}".format(emp.PredictedSalary) }}</td>
                                            <td><span class="badge bg-danger">{{ "{:.1f}".format(emp.SalaryDifference_Pct) }}%</span></td>
                                        </tr>
                                        {% endif %}
                                    {% endfor %}
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>
            </div>
            
            <!-- Market Aligned -->
            <div class="accordion-item border-success">
                <h2 class="accordion-header">
                    <button class="accordion-button collapsed bg-success bg-opacity-10" type="button" data-bs-toggle="collapse" data-bs-target="#marketAligned">
                        <i class="fa-solid fa-equals text-success me-2"></i>
                        <strong>市場對齊 (Market Aligned)</strong>
                        <span class="badge bg-success ms-2">
                            {{ prediction_data.details | selectattr('SalaryAlignment', 'equalto', 'Market Aligned') | list | length }} 人
                        </span>
                    </button>
                </h2>
                <div id="marketAligned" class="accordion-collapse collapse" data-bs-parent="#salaryAlignmentAccordion">
                    <div class="accordion-body">
                        <div class="table-responsive">
                            <table class="table table-sm table-hover">
                                <thead class="table-light">
                                    <tr>
                                        <th>員工編號</th>
                                        <th>姓名</th>
                                        <th>部門</th>
                                        <th>職位</th>
                                        <th>實際薪資</th>
                                        <th>預測薪資</th>
                                        <th>差異</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    {% for emp in prediction_data.details %}
                                        {% if emp.SalaryAlignment == 'Market Aligned' %}
                                        <tr>
                                            <td>{{ emp.EmployeeID }}</td>
                                            <td>{{ emp.FirstName }} {{ emp.LastName }}</td>
                                            <td>{{ emp.DepartmentName }}</td>
                                            <td>{{ emp.JobTitle }}</td>
                                            <td>${{ "{:,.0f}".format(emp.BaseSalary) }}</td>
                                            <td>${{ "{:,.0f}".format(emp.PredictedSalary) }}</td>
                                            <td><span class="badge bg-success">{{ "{:.1f}".format(emp.SalaryDifference_Pct) }}%</span></td>
                                        </tr>
                                        {% endif %}
                                    {% endfor %}
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>
            </div>
            
            <!-- Above Market -->
            <div class="accordion-item border-info">
                <h2 class="accordion-header">
                    <button class="accordion-button collapsed bg-info bg-opacity-10" type="button" data-bs-toggle="collapse" data-bs-target="#aboveMarket">
                        <i class="fa-solid fa-arrow-up text-info me-2"></i>
                        <strong>高於市場 (Above Market)</strong>
                        <span class="badge bg-info ms-2">
                            {{ prediction_data.details | selectattr('SalaryAlignment', 'equalto', 'Above Market') | list | length }} 人
                        </span>
                    </button>
                </h2>
                <div id="aboveMarket" class="accordion-collapse collapse" data-bs-parent="#salaryAlignmentAccordion">
                    <div class="accordion-body">
                        <div class="table-responsive">
                            <table class="table table-sm table-hover">
                                <thead class="table-light">
                                    <tr>
                                        <th>員工編號</th>
                                        <th>姓名</th>
                                        <th>部門</th>
                                        <th>職位</th>
                                        <th>實際薪資</th>
                                        <th>預測薪資</th>
                                        <th>差異</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    {% for emp in prediction_data.details %}
                                        {% if emp.SalaryAlignment == 'Above Market' %}
                                        <tr>
                                            <td>{{ emp.EmployeeID }}</td>
                                            <td>{{ emp.FirstName }} {{ emp.LastName }}</td>
                                            <td>{{ emp.DepartmentName }}</td>
                                            <td>{{ emp.JobTitle }}</td>
                                            <td>${{ "{:,.0f}".format(emp.BaseSalary) }}</td>
                                            <td>${{ "{:,.0f}".format(emp.PredictedSalary) }}</td>
                                            <td><span class="badge bg-info">+{{ "{:.1f}".format(emp.SalaryDifference_Pct) }}%</span></td>
                                        </tr>
                                        {% endif %}
                                    {% endfor %}
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

<!-- Section 3: Detailed List Card -->'''

# 替換
new_content = content.replace(marker, employee_list_section)

# 寫回檔案
with open(template_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("✅ 成功在 analysis.html 中添加員工分類詳細列表!")
