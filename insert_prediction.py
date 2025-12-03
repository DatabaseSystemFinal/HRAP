# Script to insert prediction section into analysis.html
import os

# 獲取腳本所在目錄的絕對路徑
script_dir = os.path.dirname(os.path.abspath(__file__))

# 構建 analysis.html 的相對路徑
template_path = os.path.join(script_dir, 'templates', 'analysis.html')

with open(template_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Find the insertion point (after clustering insights section, before detailed list)
marker = '<!-- Section 2: Detailed List Card -->'

prediction_section = '''<!-- Section 2: PREDICTIVE ANALYTICS -->
<div class="card shadow-sm mb-4">
    <div class="card-header bg-white py-3">
        <h5 class="mb-0 text-primary">
            <i class="fa-solid fa-brain me-2"></i>Predictive Analytics
        </h5>
    </div>
    <div class="card-body">
        <p class="text-muted mb-4">
            Machine learning predictions for employee turnover risk and salary alignment based on historical data patterns.
        </p>
        
        <div class="row g-4 mb-4">
            <!-- Turnover Risk Distribution -->
            <div class="col-md-6">
                <div class="card border-0 bg-light h-100">
                    <div class="card-body">
                        <h6 class="card-title fw-bold mb-3">
                            <i class="fa-solid fa-exclamation-triangle me-2 text-warning"></i>Turnover Risk Distribution
                        </h6>
                        <div class="table-responsive">
                            <table class="table table-sm table-borderless">
                                <tbody>
                                    {% for item in prediction_data.turnover_summary %}
                                        {% set risk_class = '' %}
                                        {% set risk_icon = '' %}
                                        {% if item.Risk_Level == 'High' %}
                                            {% set risk_class = 'text-danger' %}
                                            {% set risk_icon = 'fa-circle-xmark' %}
                                        {% elif item.Risk_Level == 'Medium' %}
                                            {% set risk_class = 'text-warning' %}
                                            {% set risk_icon = 'fa-circle-exclamation' %}
                                        {% else %}
                                            {% set risk_class = 'text-success' %}
                                            {% set risk_icon = 'fa-circle-check' %}
                                        {% endif %}
                                        <tr>
                                            <td class="fw-bold {{ risk_class }}">
                                                <i class="fa-solid {{ risk_icon }} me-2"></i>{{ item.Risk_Level }} Risk
                                            </td>
                                            <td class="text-end">{{ item.Count }} employees ({{ item.Percentage }}%)</td>
                                        </tr>
                                    {% endfor %}
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>
            </div>
            
            <!-- Salary Alignment Distribution -->
            <div class="col-md-6">
                <div class="card border-0 bg-light h-100">
                    <div class="card-body">
                        <h6 class="card-title fw-bold mb-3">
                            <i class="fa-solid fa-dollar-sign me-2 text-success"></i>Salary Alignment Distribution
                        </h6>
                        <div class="table-responsive">
                            <table class="table table-sm table-borderless">
                                <tbody>
                                    {% for item in prediction_data.salary_summary %}
                                        {% set align_class = '' %}
                                        {% set align_icon = '' %}
                                        {% if item.Alignment == 'Above Market' %}
                                            {% set align_class = 'text-info' %}
                                            {% set align_icon = 'fa-arrow-up' %}
                                        {% elif item.Alignment == 'Below Market' %}
                                            {% set align_class = 'text-danger' %}
                                            {% set align_icon = 'fa-arrow-down' %}
                                        {% else %}
                                            {% set align_class = 'text-success' %}
                                            {% set align_icon = 'fa-equals' %}
                                        {% endif %}
                                        <tr>
                                            <td class="fw-bold {{ align_class }}">
                                                <i class="fa-solid {{ align_icon }} me-2"></i>{{ item.Alignment }}
                                            </td>
                                            <td class="text-end">{{ item.Count }} employees ({{ item.Percentage }}%)</td>
                                        </tr>
                                    {% endfor %}
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        
        <!-- Model Performance Metrics -->
        <div class="alert alert-secondary border-0">
            <h6 class="fw-bold mb-2"><i class="fa-solid fa-chart-line me-2"></i>Model Performance</h6>
            <div class="row text-center">
                <div class="col-md-4">
                    <small class="text-muted d-block">Turnover Prediction Accuracy</small>
                    <strong class="fs-5 text-primary">{{ prediction_data.model_metrics.turnover_accuracy }}%</strong>
                </div>
                <div class="col-md-4">
                    <small class="text-muted d-block">Salary Prediction R² Score</small>
                    <strong class="fs-5 text-success">{{ prediction_data.model_metrics.salary_r2 }}</strong>
                </div>
                <div class="col-md-4">
                    <small class="text-muted d-block">Salary MAE</small>
                    <strong class="fs-5 text-info">${{ "{:,.0f}".format(prediction_data.model_metrics.salary_mae) }}</strong>
                </div>
            </div>
        </div>
    </div>
</div>

<!-- Section 3: Detailed List Card -->'''

# Replace Section 2 with Section 3 and insert prediction section
new_content = content.replace(marker, prediction_section)

# Write back
with open(template_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"Successfully inserted prediction section into {template_path}")
