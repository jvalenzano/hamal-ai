#!/usr/bin/env python3
"""
Agent 5: Executive Summary Generator
Generates standalone HTML executive summaries from agent outputs.
"""

import os
import re
import json
from pathlib import Path
from datetime import datetime


def extract_validation_data(validation_path):
    """Extract feasibility scores and recommendation from validation.md"""
    with open(validation_path, 'r') as f:
        content = f.read()
    
    data = {
        'composite_score': None,
        'recommendation': None,
        'dimensions': {},
        'conditions': [],
        'confidence': None
    }
    
    # Extract composite score (format: ## Composite Score: 25/50 - CONDITIONAL GO)
    score_match = re.search(r'##\s*Composite Score:\s*(\d+)/50\s*-\s*([A-Z\s]+)', content)
    if score_match:
        data['composite_score'] = int(score_match.group(1))
        data['recommendation'] = score_match.group(2).strip()
    
    # Extract confidence
    conf_match = re.search(r'\*\*Confidence:\*\*\s*(\w+)', content)
    if conf_match:
        data['confidence'] = conf_match.group(1)
    
    # Extract dimension scores (format: ### Technical Complexity: 5/10)
    dimensions = ['Technical Complexity', 'Compliance Burden', 'Stakeholder Alignment', 
                  'Timeline Pressure', 'Budget Clarity']
    for dim in dimensions:
        dim_match = re.search(rf'###\s*{dim}:\s*(\d+)/10', content)
        if dim_match:
            data['dimensions'][dim] = int(dim_match.group(1))
    
    # Extract conditions
    conditions_section = re.search(r'\*\*Conditions.*?:\*\*\s*(.*?)(?:\*\*Next Steps|\Z)', content, re.DOTALL)
    if conditions_section:
        conditions_text = conditions_section.group(1)
        conditions = re.findall(r'\d+\.\s*(.+?)(?=\n\d+\.|\n\*\*|\Z)', conditions_text, re.DOTALL)
        data['conditions'] = [c.strip() for c in conditions[:3]]  # Top 3
    
    return data


def extract_architecture_data(architecture_path):
    """Extract cost, timeline, and stack from architecture.md"""
    with open(architecture_path, 'r') as f:
        content = f.read()
    
    data = {
        'total_cost': None,
        'dev_cost': None,
        'gcp_monthly': None,
        'timeline_weeks': None,
        'dev_hours': None,
        'stack': {}
    }
    
    # Extract total cost (Look for header or specific format)
    # Matches: ### Total Project Cost\n**$80,000**
    total_match = re.search(r'### Total Project Cost.*?\n\s*\*\*?\$?([\d,]+)\*\*?', content, re.IGNORECASE | re.DOTALL)
    if total_match:
        data['total_cost'] = int(total_match.group(1).replace(',', ''))
    
    # Extract dev cost
    # Matches: - **Total Dev Cost:** $75,000
    dev_match = re.search(r'Total Dev Cost.*?\*\*?\$?([\d,]+)', content, re.IGNORECASE)
    if dev_match:
        data['dev_cost'] = int(dev_match.group(1).replace(',', ''))
    
    # Extract GCP monthly
    # Matches: - **Monthly:** $500
    monthly_match = re.search(r'Monthly.*?\*\*?\$?([\d,]+)', content, re.IGNORECASE)
    if monthly_match:
        data['gcp_monthly'] = int(monthly_match.group(1).replace(',', ''))
    
    # Extract timeline
    timeline_match = re.search(r'\*\*Duration:\*\*\s*(\d+)\s*weeks', content, re.IGNORECASE)
    if timeline_match:
        data['timeline_weeks'] = int(timeline_match.group(1))
    
    # Extract dev hours
    # Matches: - **Total Hours:** 500 hours
    hours_match = re.search(r'Total Hours.*?\*\*?\s*([\d,]+)', content, re.IGNORECASE)
    if hours_match:
        data['dev_hours'] = int(hours_match.group(1).replace(',', ''))
    
    # Extract stack (simplified)
    # Using more flexible lookaheads and case insensitivity
    stack_sections = {
        'Backend': r'\*\*Language/Framework:\*\*\s*(.+?)(?=\n)',
        'Database': r'\*\*Primary:\*\*\s*(.+?)(?=\n)',
        'AI/ML': r'\*\*Platform:\*\*\s*(.+?)(?=\n)',
        'Frontend': r'\*\*Framework:\*\*\s*(.+?)(?=\n)',
        'Deployment': r'\*\*Platform:\*\*\s*(.+?)(?=\n)'
    }
    
    for key, pattern in stack_sections.items():
        match = re.search(pattern, content, re.IGNORECASE)
        if match:
            # Clean up potential markdown artifacts
            data['stack'][key] = match.group(1).strip().strip('*')
    
    return data


def extract_problem_data(problem_path):
    """Extract core problem and severity from problem.md"""
    with open(problem_path, 'r') as f:
        content = f.read()
    
    data = {
        'core_problem': None,
        'severity': None,
        'stakeholders': []
    }
    
    # Extract core problem
    problem_match = re.search(r'## Core Problem\s*(.+?)(?=\n##)', content, re.DOTALL)
    if problem_match:
        data['core_problem'] = problem_match.group(1).strip()
    
    # Extract severity
    severity_match = re.search(r'\*\*Level:\*\*\s*(.+)', content)
    if severity_match:
        data['severity'] = severity_match.group(1).strip()
    
    # Extract stakeholders
    stakeholders_match = re.search(r'## Stakeholders\s*(.+?)(?=\n##)', content, re.DOTALL)
    if stakeholders_match:
        stakeholders_text = stakeholders_match.group(1)
        stakeholders = re.findall(r'\*\*(.+?):\*\*', stakeholders_text)
        data['stakeholders'] = stakeholders[:3]  # Top 3
    
    return data


def extract_research_data(research_path):
    """Extract key findings from research.md"""
    with open(research_path, 'r') as f:
        content = f.read()
    
    data = {
        'precedents': None,
        'competitors': None,
        'key_insight': None
    }
    
    # Extract precedents summary
    precedents_match = re.search(r'## Government Precedents.*?###\s*(.+?)\n', content, re.DOTALL)
    if precedents_match:
        data['precedents'] = precedents_match.group(1).strip()
    
    # Extract competitors summary
    competitors_match = re.search(r'## Commercial Competitors.*?###\s*(.+?)\n', content, re.DOTALL)
    if competitors_match:
        data['competitors'] = competitors_match.group(1).strip()
    
    # Extract first key insight
    insight_match = re.search(r'## Key Insights.*?\*\*(.+?)\*\*', content, re.DOTALL)
    if insight_match:
        data['key_insight'] = insight_match.group(1).strip()
    
    return data


def generate_html(data, project_name):
    """Generate standalone HTML with embedded visualizations"""
    
    # Safe value extraction with fallbacks
    def safe_int(value, default=0):
        """Safely convert to int or return default"""
        return int(value) if value is not None else default
    
    def safe_str(value, default='N/A'):
        """Safely convert to string or return default"""
        return str(value) if value is not None else default
    
    # Prepare Chart.js data
    dimension_labels = list(data['validation']['dimensions'].keys())
    dimension_values = list(data['validation']['dimensions'].values())
    
    # Extract values with safe defaults
    total_cost = safe_int(data['architecture']['total_cost'])
    dev_cost = safe_int(data['architecture']['dev_cost'])
    gcp_monthly = safe_int(data['architecture']['gcp_monthly'])
    timeline_weeks = safe_int(data['architecture']['timeline_weeks'], 12)
    dev_hours = safe_int(data['architecture']['dev_hours'])
    
    # Calculate GCP annual cost
    gcp_annual = gcp_monthly * (timeline_weeks // 4) if gcp_monthly else 0
    
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Executive Summary - {project_name}</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            line-height: 1.6;
            color: #333;
            background: #f5f5f5;
            padding: 20px;
        }}
        
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            padding: 40px;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }}
        
        header {{
            border-bottom: 3px solid #2563eb;
            padding-bottom: 20px;
            margin-bottom: 30px;
        }}
        
        h1 {{
            font-size: 2.5rem;
            color: #1e293b;
            margin-bottom: 10px;
        }}
        
        .meta {{
            color: #64748b;
            font-size: 0.9rem;
        }}
        
        .recommendation {{
            background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%);
            color: white;
            padding: 30px;
            border-radius: 8px;
            margin-bottom: 30px;
        }}
        
        .recommendation h2 {{
            font-size: 1.8rem;
            margin-bottom: 10px;
        }}
        
        .recommendation .score {{
            font-size: 3rem;
            font-weight: bold;
            margin: 10px 0;
        }}
        
        .recommendation .label {{
            font-size: 1.2rem;
            opacity: 0.9;
        }}
        
        .section {{
            margin-bottom: 40px;
        }}
        
        .section h3 {{
            font-size: 1.5rem;
            color: #1e293b;
            margin-bottom: 15px;
            border-left: 4px solid #2563eb;
            padding-left: 15px;
        }}
        
        .grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }}
        
        .card {{
            background: #f8fafc;
            padding: 20px;
            border-radius: 6px;
            border: 1px solid #e2e8f0;
        }}
        
        .card h4 {{
            font-size: 1.1rem;
            color: #475569;
            margin-bottom: 10px;
        }}
        
        .card .value {{
            font-size: 2rem;
            font-weight: bold;
            color: #2563eb;
        }}
        
        .card .label {{
            font-size: 0.9rem;
            color: #64748b;
        }}
        
        .chart-container {{
            position: relative;
            height: 400px;
            margin: 20px 0;
        }}
        
        ul {{
            list-style: none;
            padding-left: 0;
        }}
        
        ul li {{
            padding: 10px 0;
            border-bottom: 1px solid #e2e8f0;
        }}
        
        ul li:before {{
            content: "→";
            color: #2563eb;
            font-weight: bold;
            margin-right: 10px;
        }}
        
        .stack-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
            gap: 15px;
        }}
        
        .stack-item {{
            background: #f1f5f9;
            padding: 15px;
            border-radius: 4px;
        }}
        
        .stack-item .stack-label {{
            font-size: 0.8rem;
            color: #64748b;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}
        
        .stack-item .stack-value {{
            font-size: 1rem;
            color: #1e293b;
            font-weight: 500;
            margin-top: 5px;
        }}
        
        @media print {{
            body {{
                background: white;
                padding: 0;
            }}
            .container {{
                box-shadow: none;
                padding: 20px;
            }}
            .chart-container {{
                page-break-inside: avoid;
            }}
        }}
        
        @media (max-width: 768px) {{
            .container {{
                padding: 20px;
            }}
            h1 {{
                font-size: 2rem;
            }}
            .recommendation .score {{
                font-size: 2rem;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>Executive Summary</h1>
            <div class="meta">
                <strong>Project:</strong> {project_name} | 
                <strong>Generated:</strong> {datetime.now().strftime('%B %d, %Y')} |
                <strong>Confidence:</strong> {data['validation'].get('confidence', 'N/A')}
            </div>
        </header>
        
        <div class="recommendation">
            <h2>Recommendation</h2>
            <div class="score">{data['validation']['composite_score']}/50</div>
            <div class="label">{data['validation']['recommendation']}</div>
        </div>
        
        <div class="section">
            <h3>Problem Statement</h3>
            <p>{data['problem']['core_problem']}</p>
            <p style="margin-top: 10px;"><strong>Severity:</strong> {data['problem']['severity']}</p>
        </div>
        
        <div class="section">
            <h3>Investment Required</h3>
            <div class="grid">
                <div class="card">
                    <h4>Total Project Cost</h4>
                    <div class="value">${total_cost:,}</div>
                    <div class="label">Development + Infrastructure</div>
                </div>
                <div class="card">
                    <h4>Timeline</h4>
                    <div class="value">{timeline_weeks}</div>
                    <div class="label">Weeks to Production</div>
                </div>
                <div class="card">
                    <h4>Development Effort</h4>
                    <div class="value">{dev_hours:,}</div>
                    <div class="label">Total Hours</div>
                </div>
                <div class="card">
                    <h4>Monthly GCP Cost</h4>
                    <div class="value">${gcp_monthly:,}</div>
                    <div class="label">Ongoing Infrastructure</div>
                </div>
            </div>
        </div>
        
        <div class="section">
            <h3>Feasibility Assessment</h3>
            <div class="chart-container">
                <canvas id="feasibilityChart"></canvas>
            </div>
        </div>
        
        <div class="section">
            <h3>Cost Breakdown</h3>
            <div class="chart-container" style="height: 300px;">
                <canvas id="costChart"></canvas>
            </div>
        </div>
        
        <div class="section">
            <h3>Key Research Findings</h3>
            <ul>
                <li><strong>Government Precedents:</strong> {data['research']['precedents'] or 'None identified'}</li>
                <li><strong>Commercial Competitors:</strong> {data['research']['competitors'] or 'None identified'}</li>
                <li><strong>Key Insight:</strong> {data['research']['key_insight'] or 'See research.md for details'}</li>
            </ul>
        </div>
        
        <div class="section">
            <h3>Recommended Tech Stack</h3>
            <div class="stack-grid">
                {''.join([f'''
                <div class="stack-item">
                    <div class="stack-label">{key}</div>
                    <div class="stack-value">{value}</div>
                </div>
                ''' for key, value in data['architecture']['stack'].items()])}
            </div>
        </div>
        
        <div class="section">
            <h3>Conditions for Success</h3>
            <ul>
                {''.join([f'<li>{condition}</li>' for condition in data['validation']['conditions']])}
            </ul>
        </div>
    </div>
    
    <script>
        // Feasibility Radar Chart
        const feasibilityCtx = document.getElementById('feasibilityChart').getContext('2d');
        new Chart(feasibilityCtx, {{
            type: 'radar',
            data: {{
                labels: {json.dumps(dimension_labels)},
                datasets: [{{
                    label: 'Feasibility Score',
                    data: {json.dumps(dimension_values)},
                    backgroundColor: 'rgba(37, 99, 235, 0.2)',
                    borderColor: 'rgba(37, 99, 235, 1)',
                    borderWidth: 2,
                    pointBackgroundColor: 'rgba(37, 99, 235, 1)',
                    pointBorderColor: '#fff',
                    pointHoverBackgroundColor: '#fff',
                    pointHoverBorderColor: 'rgba(37, 99, 235, 1)'
                }}]
            }},
            options: {{
                scales: {{
                    r: {{
                        beginAtZero: true,
                        max: 10,
                        ticks: {{
                            stepSize: 2
                        }}
                    }}
                }},
                plugins: {{
                    legend: {{
                        display: false
                    }}
                }}
            }}
        }});
        
        // Cost Breakdown Bar Chart
        const costCtx = document.getElementById('costChart').getContext('2d');
        new Chart(costCtx, {{
            type: 'bar',
            data: {{
                labels: ['Development', 'GCP Infrastructure ({timeline_weeks // 4} months)'],
                datasets: [{{
                    label: 'Cost ($)',
                    data: [{dev_cost}, {gcp_annual}],
                    backgroundColor: [
                        'rgba(37, 99, 235, 0.8)',
                        'rgba(59, 130, 246, 0.8)'
                    ],
                    borderColor: [
                        'rgba(37, 99, 235, 1)',
                        'rgba(59, 130, 246, 1)'
                    ],
                    borderWidth: 1
                }}]
            }},
            options: {{
                indexAxis: 'y',
                scales: {{
                    x: {{
                        beginAtZero: true,
                        ticks: {{
                            callback: function(value) {{
                                return '$' + value.toLocaleString();
                            }}
                        }}
                    }}
                }},
                plugins: {{
                    legend: {{
                        display: false
                    }}
                }}
            }}
        }});
    </script>
</body>
</html>
"""
    
    return html


def main(project_dir):
    """Main entry point"""
    try:
        project_path = Path(project_dir)
        
        if not project_path.exists():
            print(f"Error: Project directory not found: {project_dir}")
            return 1
        
        print(f"Extracting data from {project_dir}...")
        
        # Extract data from all agent outputs
        data = {
            'validation': extract_validation_data(project_path / 'validation.md'),
            'architecture': extract_architecture_data(project_path / 'architecture.md'),
            'problem': extract_problem_data(project_path / 'problem.md'),
            'research': extract_research_data(project_path / 'research.md')
        }
        
        print(f"Data extracted successfully")
        
        # Get project name from directory
        project_name = project_path.name.replace('-', ' ').title()
        
        print(f"Generating HTML for {project_name}...")
        
        # Generate HTML
        html = generate_html(data, project_name)
        
        print(f"HTML generated ({len(html)} bytes)")
        
        # Write to file
        output_path = project_path / 'summary.html'
        with open(output_path, 'w') as f:
            f.write(html)
        
        print(f"✅ Executive summary generated: {output_path}")
        return 0
    
    except Exception as e:
        print(f"❌ Error generating summary: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python summary.py <project_directory>")
        sys.exit(1)
    
    sys.exit(main(sys.argv[1]))
