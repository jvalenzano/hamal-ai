import pytest
import os
from unittest.mock import patch, mock_open
from agents.summary import (
    extract_validation_data,
    extract_architecture_data,
    extract_problem_data,
    extract_research_data
)

def test_extract_validation_data():
    """Test data extraction from validation.md"""
    mock_content = """
## Composite Score: 35/50 - CONDITIONAL GO
**Confidence:** High

### Technical Complexity: 6/10
### Compliance Burden: 4/10
### Stakeholder Alignment: 8/10
### Timeline Pressure: 7/10
### Budget Clarity: 5/10

**Conditions for Success:**
1. Condition A
2. Condition B
3. Condition C

**Next Steps**
Follow up.
"""
    
    with patch("builtins.open", mock_open(read_data=mock_content.strip())):
        data = extract_validation_data("dummy_path")
        
    assert data["composite_score"] == 35
    assert data["recommendation"] == "CONDITIONAL GO"
    assert data["confidence"] == "High"
    assert data["dimensions"]["Technical Complexity"] == 6
    assert data["dimensions"]["Budget Clarity"] == 5
    assert len(data["conditions"]) == 3
    assert data["conditions"][0] == "Condition A"

def test_extract_architecture_data():
    """Test data extraction from architecture.md"""
    mock_content = """
**$150,000** (Dev
Dev $150,000
Monthly Total:** $2,500
**Duration:** 12 weeks
Total Hours:** 1,200

**Language/Framework:** Python/FastAPI
**Primary:** PostgreSQL
**Platform:** OpenAI
**Framework:** React
**Platform:** GCP Cloud Run
"""
    
    with patch("builtins.open", mock_open(read_data=mock_content.strip())):
        data = extract_architecture_data("dummy_path")
        
    assert data["total_cost"] == 150000
    assert data["dev_cost"] == 150000
    assert data["gcp_monthly"] == 2500
    assert data["timeline_weeks"] == 12
    assert data["dev_hours"] == 1200
    assert data["stack"]["Backend"] == "Python/FastAPI"
    assert data["stack"]["Database"] == "PostgreSQL"
    assert data["stack"]["AI/ML"] == "OpenAI"

def test_extract_problem_data():
    """Test data extraction from problem.md"""
    mock_content = """
## Core Problem
This is the core problem statement.

## Pain Severity
**Level:** High

## Stakeholders
**Stakeholder 1:** Description 1
**Stakeholder 2:** Description 2

## Next Section
"""
    
    with patch("builtins.open", mock_open(read_data=mock_content.strip())):
        data = extract_problem_data("dummy_path")
        
    assert data["core_problem"] == "This is the core problem statement."
    assert data["severity"] == "High"
    assert "Stakeholder 1" in data["stakeholders"]
    assert "Stakeholder 2" in data["stakeholders"]

def test_extract_research_data():
    """Test data extraction from research.md"""
    mock_content = """
## Government Precedents
### Precedent Title

## Commercial Competitors
### Competitor Title

## Key Insights
**Key insight 1**
"""
    
    with patch("builtins.open", mock_open(read_data=mock_content.strip())):
        data = extract_research_data("dummy_path")
        
    assert data["precedents"] == "Precedent Title"
    assert data["competitors"] == "Competitor Title"
    assert data["key_insight"] == "Key insight 1"
