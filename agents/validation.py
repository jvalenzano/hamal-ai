#!/usr/bin/env python3
"""
Validation Agent - Feasibility Scoring & Risk Analysis

Purpose: Score project on 5 dimensions, identify risks
Method: LLM-based scoring with domain-specific rubric
Output: validation.md (feasibility score, risk register)
"""

import os
import json
import sys
import logging
import warnings

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents.utils import call_llm, get_response_content, DEFAULT_MODEL, FatalError, log_verbose, clean_json_output
from dotenv import load_dotenv

load_dotenv()

# Suppress Pydantic serialization warnings
warnings.filterwarnings('ignore', message='.*Pydantic serializer warnings.*')
warnings.filterwarnings('ignore', category=UserWarning, module='pydantic')

logger = logging.getLogger(__name__)

# claude = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))


def score_feasibility(problem_md: str, research_md: str) -> dict:
    """
    Score project on 5 dimensions (0-10 each).
    
    Dimensions:
    1. Technical Complexity (data integration? real-time? scale?)
    2. Compliance Burden (FedRAMP? PII/CUI? 508?)
    3. Stakeholder Alignment (single agency? multi-agency? executive sponsor?)
    4. Timeline Pressure (urgent? flexible? unknown?)
    5. Budget Clarity (approved? TBD? competitive bid?)
    
    Returns dict with scores + reasoning.
    """
    
    system_prompt = """You are a federal project feasibility analyst for TechTrend.

Score this project on 5 dimensions (0-10 each):

**Scoring rubric:**
- 0-3: High risk (red flag, likely blocker)
- 4-7: Medium risk (mitigatable with planning)
- 8-10: Low risk (favorable, proceed confidently)

**Dimensions:**

1. **Technical Complexity** (0-10)
   - Data integration complexity (single source = 10, multi-format = 5, real-time = 2)
   - AI/ML requirements (proven tech = 10, experimental = 3)
   - Scale (hundreds of users = 10, millions = 5)

2. **Compliance Burden** (0-10)
   - FedRAMP (not required = 10, Moderate = 6, High = 3)
   - PII/CUI handling (none = 10, moderate = 6, extensive = 3)
   - 508 Accessibility (standard dashboard = 8, complex interactions = 5)

3. **Stakeholder Alignment** (0-10)
   - Single agency lead = 10, multi-agency coordination = 5, no clear owner = 2
   - Executive sponsorship (charter-level = 10, middle management = 6, grassroots = 3)

4. **Timeline Pressure** (0-10)
   - Flexibility (no deadline = 10, seasonal = 7, urgent = 4, ASAP = 2)
   - Realistic expectations (understands MVP = 10, wants everything = 3)

5. **Budget Clarity** (0-10)
   - Approved budget = 10, "think we have funding" = 6, competitive bid = 4, unknown = 2
   - Procurement vehicle (existing contract = 10, new RFP = 5)

**Output JSON:**
```json
{
  "technical_complexity": {
    "score": X,
    "reasoning": "..."
  },
  "compliance_burden": {
    "score": X,
    "reasoning": "..."
  },
  "stakeholder_alignment": {
    "score": X,
    "reasoning": "..."
  },
  "timeline_pressure": {
    "score": X,
    "reasoning": "..."
  },
  "budget_clarity": {
    "score": X,
    "reasoning": "..."
  },
  "composite_score": XX,
  "recommendation": "GO / CONDITIONAL GO / NO-GO"
}
```

**Recommendation thresholds:**
- 40-50: GO (high confidence)
- 30-39: CONDITIONAL GO (mitigate key risks first)
- 0-29: NO-GO (too many red flags)
"""
    
    response = call_llm(
        model="claude-sonnet-4-20250514",
        max_tokens=2048,
        system=system_prompt,
        messages=[{
            "role": "user",
            "content": f"""Score this project:

## Problem Statement:
{problem_md}

## Research Findings:
{research_md}

Return JSON with scores for all 5 dimensions."""
        }]
    )
    
    # Parse JSON
    try:
        scores = json.loads(clean_json_output(get_response_content(response)))
    except json.JSONDecodeError:
        # Fallback if parsing fails
        logger.warning("Could not parse scoring JSON, using defaults")
        scores = {
            "composite_score": 25,
            "recommendation": "CONDITIONAL GO"
        }
    
    return scores


def analyze_risks(problem_md: str, research_md: str, scores: dict) -> dict:
    """
    Identify riskiest assumptions and red flags.
    
    Returns dict with:
    - riskiest_assumptions: list (what must be true?)
    - red_flags: list (warning signs from research)
    - mitigation_strategies: list (how to de-risk)
    """
    
    system_prompt = """You are a risk analyst for government AI projects.

Identify:

1. **Riskiest Assumptions** (top 3)
   - What must be true for this project to succeed?
   - For each, estimate: probability (%), impact (Critical/High/Medium), mitigation

2. **Red Flags** (warning signs)
   - From research: Did similar projects fail? Why?
   - From problem: Are expectations unrealistic? (real-time when batch is more realistic?)
   - From stakeholders: Multi-agency coordination without MOA?

3. **Mitigation Strategies**
   - For each risk, recommend how to de-risk
   - Examples: "Prototype with synthetic data first", "Technical spike in Week 1 to validate OCR accuracy"

**Output JSON:**
```json
{
  "riskiest_assumptions": [
    {
      "assumption": "...",
      "probability": "60%",
      "impact": "Critical/High/Medium",
      "mitigation": "..."
    }
  ],
  "red_flags": [
    "..."
  ],
  "mitigation_strategies": [
    "..."
  ]
}
```
"""
    
    response = call_llm(
        model="claude-sonnet-4-20250514",
        max_tokens=2048,
        system=system_prompt,
        messages=[{
            "role": "user",
            "content": f"""Analyze risks for this project:

## Problem:
{problem_md}

## Research:
{research_md}

## Feasibility Scores:
{json.dumps(scores, indent=2)}

Return JSON with riskiest assumptions, red flags, mitigation strategies."""
        }]
    )
    
    # Parse JSON
    try:
        risks = json.loads(clean_json_output(get_response_content(response)))
    except json.JSONDecodeError:
        logger.warning("Could not parse risk JSON, using defaults")
        risks = {
            "riskiest_assumptions": [],
            "red_flags": [],
            "mitigation_strategies": []
        }
    
    return risks


def generate_validation_report(scores: dict, risks: dict) -> str:
    """
    Synthesize scores + risks into validation.md
    """
    
    system_prompt = """You are generating a validation report.

Format (markdown):

# Feasibility Assessment

## Composite Score: X/50 - [GO / CONDITIONAL GO / NO-GO]

**Confidence:** [High/Medium/Low]

***

## Dimension Scores

### Technical Complexity: X/10
[Reasoning from scores]

### Compliance Burden: X/10
[Reasoning from scores]

### Stakeholder Alignment: X/10
[Reasoning from scores]

### Timeline Pressure: X/10
[Reasoning from scores]

### Budget Clarity: X/10
[Reasoning from scores]

***

## Risk Register

### Riskiest Assumptions

1. **[Assumption]**
   - **Probability:** X%
   - **Impact:** Critical/High/Medium
   - **Mitigation:** [How to de-risk]

[Repeat for top 3]

### Red Flags

- [Flag 1 from research/problem]
- [Flag 2]
- [Flag 3]

***

## Recommended Mitigation Strategies

1. [Strategy 1]
2. [Strategy 2]
3. [Strategy 3]

***

## Decision Recommendation

**Recommendation:** [GO / CONDITIONAL GO / NO-GO]

**Rationale:** [Why this recommendation based on scores + risks]

**Conditions (if CONDITIONAL GO):**
1. [Condition that must be met before proceeding]
2. [Condition 2]

**Next Steps:**
1. [Immediate action - e.g., "Schedule stakeholder alignment meeting"]
2. [Follow-up - e.g., "Technical spike to validate OCR accuracy"]
"""
    
    response = call_llm(
        model="claude-sonnet-4-20250514",
        max_tokens=3000,
        system=system_prompt,
        messages=[{
            "role": "user",
            "content": f"""Generate validation report:

## Scores:
{json.dumps(scores, indent=2)}

## Risks:
{json.dumps(risks, indent=2)}

Follow themarkdown format template."""
        }]
    )
    
    return get_response_content(response)


def run_validation(project_dir: str) -> str:
    """
    Full validation pipeline.
    
    Args:
        project_dir: Path to outputs/[project-name]/
    
    Returns: path to generated validation.md
    """
    
    # Read inputs
    problem_path = os.path.join(project_dir, "problem.md")
    research_path = os.path.join(project_dir, "research.md")
    
    try:
        log_verbose(f"Reading problem.md from {problem_path}")
        with open(problem_path, "r") as f:
            problem_md = f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Missing required file: {problem_path}. Run Discovery agent first.")
    except Exception as e:
        raise Exception(f"Error reading problem.md: {e}")
    
    try:
        log_verbose(f"Reading research.md from {research_path}")
        with open(research_path, "r") as f:
            research_md = f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Missing required file: {research_path}. Run Research agent first.")
    except Exception as e:
        raise Exception(f"Error reading research.md: {e}")
    
    logger.info("📊 Validation Agent: Scoring feasibility...")
    scores = score_feasibility(problem_md, research_md)
    logger.info(f"   Composite Score: {scores.get('composite_score', 'N/A')}/50")
    
    logger.info("\n⚠️  Validation Agent: Analyzing risks...")
    risks = analyze_risks(problem_md, research_md, scores)
    logger.info(f"   Identified {len(risks.get('riskiest_assumptions', []))} key assumptions")
    
    logger.info("\n📝 Validation Agent: Generating report...")
    validation_md = generate_validation_report(scores, risks)
    
    # Save output
    output_path = os.path.join(project_dir, "validation.md")
    with open(output_path, "w") as f:
        f.write(validation_md)
    
    logger.info(f"\n✅ Validation Agent complete: {output_path}")
    
    return output_path


# CLI Interface
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python agents/validation.py outputs/<project>/")
        print("\nExample:")
        print("  python agents/validation.py outputs/ranger/")
        sys.exit(1)
    
    project_dir = sys.argv[1].rstrip("/")
    
    if not os.path.exists(project_dir):
        print(f"Error: Directory not found: {project_dir}")
        sys.exit(1)
    
    # Verify required files exist
    required = ["problem.md", "research.md"]
    for filename in required:
        if not os.path.exists(os.path.join(project_dir, filename)):
            print(f"Error: Missing required file: {filename}")
            print("Run Discovery and Research agents first.")
            sys.exit(1)
    
    output = run_validation(project_dir)
    
    print("\n" + "="*60)
    print("VALIDATION COMPLETE")
    print("="*60)
    print(f"Output: {output}")
    print("\nNext steps:")
    print("1. Review validation.md")
    print("2. If CONDITIONAL GO or GO, run Architecture Agent")
