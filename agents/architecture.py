#!/usr/bin/env python3
"""
Architecture Agent - Stack Recommendation & Cost Estimation

Purpose: Generate buildable architecture based on similar historical projects
Method: Similarity search + LLM-based stack recommendation
Output: architecture.md (stack, costs, timeline, reusable components)
"""

import os
import json
import sys
import logging
import warnings

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents.utils import call_llm, get_response_content, FAST_MODEL, FatalError, log_verbose, clean_json_output
import numpy as np
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv

load_dotenv()

# Suppress Pydantic serialization warnings
warnings.filterwarnings('ignore', message='.*Pydantic serializer warnings.*')
warnings.filterwarnings('ignore', category=UserWarning, module='pydantic')

logger = logging.getLogger(__name__)

# claude = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

# Load embedding model (for similarity search)
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')


# ... (existing imports)

def extract_json(text: str) -> dict:
    """Extract JSON from text, handling markdown blocks."""
    try:
        # Try direct parse
        return json.loads(text)
    except json.JSONDecodeError:
        # Try finding markdown block
        if "```json" in text:
            text = text.split("```json")[1].split("```")[0].strip()
        elif "```" in text:
            text = text.split("```")[1].split("```")[0].strip()
        return json.loads(text)


def load_project_history() -> list:

    """Load project history from data/projects.json"""
    with open("data/projects.json", "r") as f:
        return json.load(f)


def find_similar_projects(problem_md: str, project_history: list) -> list:
    """
    Find similar historical projects using semantic similarity.
    
    Returns top 3 most similar projects.
    """
    
    # Extract problem description
    problem_embedding = embedding_model.encode(problem_md)
    
    # Compute similarity scores
    similarities = []
    for project in project_history:
        project_text = f"{project['problem']} {' '.join(project.get('stack', []))}"
        project_embedding = embedding_model.encode(project_text)
        
        # Cosine similarity
        similarity = np.dot(problem_embedding, project_embedding) / (
            np.linalg.norm(problem_embedding) * np.linalg.norm(project_embedding)
        )
        
        similarities.append({
            "project": project,
            "similarity": float(similarity)
        })
    
    # Sort by similarity
    similarities.sort(key=lambda x: x["similarity"], reverse=True)
    
    return similarities[:3]


def recommend_stack(problem_md: str, validation_md: str, similar_projects: list) -> dict:
    """
    Recommend tech stack based on:
    - Hamal defaults (FastAPI, React, Vertex AI, AlloyDB)
    - Project-specific needs (from problem/validation)
    - Similar project patterns
    
    Returns dict with stack recommendation + reasoning.
    """
    
    system_prompt = """You are a technical architect.

**Preferred Tech Stack:**
- **Backend:** Python (FastAPI)
- **Database:** AlloyDB (PostgreSQL-compatible, GCP-native)
- **AI/ML:** Vertex AI (Gemini, PaLM, custom models)
- **Storage:** Cloud Storage (files, documents)
- **Frontend:** React (PWA for offline capability)
- **Styling:** Tailwind CSS
- **Hosting:** Cloud Run (containers) or Firebase
- **Deployment:** Google Cloud Platform

**Adjust based on:**
1. **Data complexity** (multi-format ingestion → add Cloud Vision, Document AI)
2. **Real-time needs** (if truly required → add Pub/Sub, but discourage)
3. **Offline requirements** (PWA with service workers)
4. **Compliance** (FedRAMP Moderate → Assured Workloads)
5. **Similar projects** (reuse proven patterns)

**Output JSON:**
```json
{
  "backend": {
    "language": "Python 3.11",
    "framework": "FastAPI",
    "reasoning": "..."
  },
  "database": {
    "primary": "AlloyDB",
    "reasoning": "..."
  },
  "ai_ml": {
    "platform": "Vertex AI",
    "models": ["Gemini 1.5 Pro", "..."],
    "reasoning": "..."
  },
  "frontend": {
    "framework": "React",
    "features": ["PWA", "Offline-first"],
    "reasoning": "..."
  },
  "storage": {
    "primary": "Cloud Storage",
    "reasoning": "..."
  },
  "deployment": {
    "platform": "GCP",
    "services": ["Cloud Run", "Assured Workloads"],
    "reasoning": "..."
  },
  "reusable_components": [
    {
      "from_project": "RANGER",
      "component": "Multi-format document ingestion pipeline",
      "estimated_time_saved": "40 hours"
    }
  ]
}
```
"""
    
    similar_projects_text = json.dumps([s["project"] for s in similar_projects], indent=2)
    
    response = call_llm(
        model="claude-sonnet-4-5",
        max_tokens=3000,
        system=system_prompt,
        messages=[{
            "role": "user",
            "content": f"""Recommend tech stack for this project:

## Problem:
{problem_md}

## Validation:
{validation_md}

## Similar Projects:
{similar_projects_text}

Return JSON with stack recommendation + reusable components."""
        }]
    )
    
    try:
        stack = json.loads(clean_json_output(get_response_content(response)))
    except Exception as e:
        logger.warning(f"Could not parse stack JSON: {e}, using defaults")
        stack = {"backend": {"framework": "FastAPI"}}
    
    return stack


def estimate_costs(stack: dict, validation_scores: dict) -> dict:
    """
    Estimate costs:
    - GCP runtime (compute, storage, AI APIs)
    - Dev hours (based on complexity from validation)
    
    Returns dict with cost breakdown.
    """
    
    system_prompt = """You are estimating project costs.

**Assumptions:**
- **Developer rate:** $150/hour (blended)
- **GCP costs:** Typical ranges for government MVPs
  - Cloud Run: $50-200/month (depending on scale)
  - AlloyDB: $300-800/month (depending on HA requirements)
  - Vertex AI: $100-500/month (depending on usage)
  - Cloud Storage: $20-100/month
- **Timeline:** 6 weeks = $40-50K, 12 weeks = $75-90K, 16 weeks = $100-120K

**Based on complexity scores:**
- Technical Complexity 8-10 → 6 weeks
- Technical Complexity 5-7 → 12 weeks
- Technical Complexity 0-4 → 16 weeks

**Output JSON:**
```json
{
  "dev_cost": {
    "hours": X,
    "hourly_rate": 150,
    "total": $X,
    "breakdown": {
      "design": "X hours",
      "backend": "X hours",
      "frontend": "X hours",
      "ai_ml": "X hours",
      "testing_deployment": "X hours"
    }
  },
  "gcp_runtime": {
    "monthly": $X,
    "annual": $X,
    "breakdown": {
      "compute": "$X",
      "database": "$X",
      "ai_apis": "$X",
      "storage": "$X"
    }
  },
  "total_project_cost": $X,
  "timeline_weeks": X
}
```
"""
    
    response = call_llm(
        model="claude-sonnet-4-5",
        max_tokens=2000,
        system=system_prompt,
        messages=[{
            "role": "user",
            "content": f"""Estimate costs:

## Stack:
{json.dumps(stack, indent=2)}

## Complexity Scores:
Technical Complexity: {validation_scores.get('technical_complexity', {}).get('score', 5)}/10
Compliance Burden: {validation_scores.get('compliance_burden', {}).get('score', 5)}/10

Return JSON with cost estimates."""
        }]
    )
    
    try:
        costs = json.loads(clean_json_output(get_response_content(response)))
    except Exception as e:
        logger.warning(f"Could not parse cost JSON: {e}, using defaults")
        costs = {"total_project_cost": 80000, "timeline_weeks": 12}
    
    return costs


def build_timeline(complexity_scores: dict, timeline_weeks: int) -> list:
    """
    Generate week-by-week timeline with milestones.
    
    Returns list of milestones.
    """
    
    system_prompt = """You are creating a project timeline.

**Standard project phases:**
1. **Design Phase** (Weeks 1-2): Architecture, mockups, data flow diagrams
2. **Backend Development** (Weeks 3-X): APIs, data pipeline, AI integration
3. **Frontend Development** (Weeks 4-X): UI, dashboard, user testing
4. **Testing & Deployment** (Final 2 weeks): Security review, ATO prep, pilot deployment

**Output JSON:**
```json
{
  "milestones": [
    {
      "week": 1,
      "phase": "Design",
      "deliverable": "Architecture diagrams + API spec",
      "dependencies": []
    },
    {
      "week": 2,
      "phase": "Design",
      "deliverable": "Low-fi mockups + data flow",
      "dependencies": ["Week 1 complete"]
    }
  ]
}
```
"""
    
    response = call_llm(
        model="claude-sonnet-4-5",
        max_tokens=2000,
        system=system_prompt,
        messages=[{
            "role": "user",
            "content": f"""Generate {timeline_weeks}-week timeline with milestones.

Complexity: {complexity_scores.get('technical_complexity', {}).get('score', 5)}/10

Return JSON with weekly milestones."""
        }]
    )
    
    try:
        timeline = json.loads(clean_json_output(get_response_content(response)))
        return timeline.get("milestones", [])
    except Exception as e:
        logger.warning(f"Could not parse timeline JSON: {e}, using defaults")
        return []


def generate_architecture_report(stack: dict, costs: dict, timeline: list, similar_projects: list) -> str:
    """
    Synthesize into architecture.md
    """
    
    system_prompt = """Generate architecture report (markdown):

# Technical Architecture

## Recommended Stack

### Backend
- **Language/Framework:** [from stack]
- **Reasoning:** [why this choice]

### Database
- **Primary:** [from stack]
- **Reasoning:** [why this choice]

### AI/ML
- **Platform:** [from stack]
- **Models:** [list]
- **Reasoning:** [why these models]

### Frontend
- **Framework:** [from stack]
- **Key Features:** [PWA, offline, etc.]
- **Reasoning:** [why this choice]

### Deployment
- **Platform:** [GCP]
- **Services:** [Cloud Run, Assured Workloads, etc.]
- **Compliance:** [FedRAMP Moderate if required]

---

## Cost Estimate

### Development Costs
- **Total Hours:** X hours
- **Rate:** $150/hour
- **Total Dev Cost:** $X

**Breakdown:**
- Design: X hours
- Backend: X hours
- Frontend: X hours
- AI/ML: X hours
- Testing/Deployment: X hours

### GCP Runtime Costs
- **Monthly:** $X
- **Annual:** $X

**Breakdown:**
- Compute (Cloud Run): $X
- Database (AlloyDB): $X
- AI APIs (Vertex AI): $X
- Storage: $X

### Total Project Cost
**$X** (Dev + 6 months GCP runtime)

---

## Timeline

**Duration:** X weeks

| Week | Phase | Deliverable | Dependencies |
|------|-------|-------------|--------------|
| [from timeline] |

---

## Reusable Components

### From Similar Projects

[List components from similar_projects that can be reused, with time savings]

---

## Risk Mitigation (Architecture Perspective)

[Technical risks and how architecture addresses them]

---

**Recommendation:** [Proceed with this stack / Adjust X before proceeding]
"""
    
    response = call_llm(
        model="claude-sonnet-4-5",
        max_tokens=4000,
        system=system_prompt,
        messages=[{
            "role": "user",
            "content": f"""Generate architecture report:

## Stack:
{json.dumps(stack, indent=2)}

## Costs:
{json.dumps(costs, indent=2)}

## Timeline:
{json.dumps(timeline, indent=2)}

## Similar Projects:
{json.dumps([s["project"] for s in similar_projects], indent=2)}

Follow markdown template."""
        }]
    )
    
    return get_response_content(response)


def run_architecture(project_dir: str) -> str:
    """
    Full architecture pipeline.
    
    Returns: path to generated architecture.md
    """
    
    # Read inputs
    problem_path = os.path.join(project_dir, "problem.md")
    validation_path = os.path.join(project_dir, "validation.md")
    
    try:
        log_verbose(f"Reading problem.md from {problem_path}")
        with open(problem_path, "r") as f:
            problem_md = f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Missing required file: {problem_path}. Run Discovery agent first.")
    except Exception as e:
        raise Exception(f"Error reading problem.md: {e}")
    
    try:
        log_verbose(f"Reading validation.md from {validation_path}")
        with open(validation_path, "r") as f:
            validation_md = f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Missing required file: {validation_path}. Run Validation agent first.")
    except Exception as e:
        raise Exception(f"Error reading validation.md: {e}")
    
    project_name = os.path.basename(project_dir)
    
    logger.info("📚 Architecture Agent: Loading project history...")
    project_history = load_project_history()
    
    logger.info("🔍 Architecture Agent: Finding similar projects...")
    similar_projects = find_similar_projects(problem_md, project_history)
    logger.info(f"   Found {len(similar_projects)} similar projects")
    for s in similar_projects:
        logger.debug(f"     - {s['project']['name']} (similarity: {s['similarity']:.2f})")
    
    logger.info("\n🏗️  Architecture Agent: Recommending stack...")
    # Extract validation scores (parse from validation_md - simplified for POC)
    validation_scores = {"technical_complexity": {"score": 7}}  # Default
    stack = recommend_stack(problem_md, validation_md, similar_projects)
    
    logger.info("\n💰 Architecture Agent: Estimating costs...")
    costs = estimate_costs(stack, validation_scores)
    logger.info(f"   Estimated: ${costs.get('total_project_cost', 'N/A')} ({costs.get('timeline_weeks', 'N/A')} weeks)")
    
    logger.info("\n📅 Architecture Agent: Building timeline...")
    timeline = build_timeline(validation_scores, costs.get('timeline_weeks', 12))
    
    logger.info("\n📝 Architecture Agent: Generating report...")
    architecture_md = generate_architecture_report(stack, costs, timeline, similar_projects)
    
    # Save output
    output_path = os.path.join(project_dir, "architecture.md")
    with open(output_path, "w") as f:
        f.write(architecture_md)
    
    logger.info(f"\n✅ Architecture Agent complete: {output_path}")
    
    return output_path


# CLI Interface
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python agents/architecture.py outputs/<project>/")
        print("\\nExample:")
        print("  python agents/architecture.py outputs/ranger/")
        sys.exit(1)
    
    project_dir = sys.argv[1].rstrip("/")
    
    if not os.path.exists(project_dir):
        print(f"Error: Directory not found: {project_dir}")
        sys.exit(1)
    
    # Verify required files
    required = ["problem.md", "validation.md"]
    for filename in required:
        if not os.path.exists(os.path.join(project_dir, filename)):
            print(f"Error: Missing {filename}")
            sys.exit(1)
    
    output = run_architecture(project_dir)
    
    print("\\n" + "="*60)
    print("ARCHITECTURE COMPLETE")
    print("="*60)
    print(f"Output: {output}")
