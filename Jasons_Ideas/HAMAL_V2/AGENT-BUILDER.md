# ANTIGRAVITY AGENT PROMPTS - HAMAL BUILD
**Generated:** January 10, 2026, 3:39 PM PST  
**For:** TechTrend AI Factory - Hamal Project  
**Launch Strategy:** Phase 1 (4 agents parallel) → Phase 2 (2 agents sequential) → Phase 3 (1 agent)

***

# PHASE 1: FOUNDATION AGENTS (LAUNCH IN PARALLEL)

***

## AGENT 1: REPO ARCHITECT

**Launch:** Phase 1 (No dependencies)  
**Estimated Time:** 30-45 minutes  
**Output Files:** Folder structure, config files, documentation, seed data

### PROMPT:

```markdown
# Agent 1: Repo Architect - Hamal Framework

**Date:** January 10, 2026  
**Project:** Hamal @ TechTrend (AI-powered validation framework for government AI projects)  
**Your Role:** Create foundational repository structure, configuration, and documentation

---

## Context: What is Hamal?

Hamal is an **agentic research swarm** that transforms rough government agency requests (emails, charters, meeting notes) into validated, buildable project specifications. When TechTrend receives an opportunity like "Forest Service needs AI for post-fire recovery," Hamal autonomously:

1. Interrogates the problem (5 Whys, stakeholder mapping)
2. Researches precedents (similar gov projects, competitors, failures)
3. Assesses feasibility (technical complexity, compliance burden, timeline, cost)
4. Generates architecture (stack recommendations, cost estimates, risk mitigation)
5. Produces decision report (Go/No-Go with evidence)

**Key Philosophy:** This is a PROOF-OF-CONCEPT. We're testing agent prompts, not building production infrastructure. Functional > perfect. Speed > elegance. See `KEEP_IT_SIMPLE.md` for details.

---

## Your Task

Create the foundational repository structure for Hamal. This includes:

1. **Folder structure** (agents, data, outputs, tests)
2. **Configuration files** (requirements.txt, .env.example, .gitignore)
3. **Documentation** (README.md, KEEP_IT_SIMPLE.md)
4. **Seed data** (TechTrend project history, domain context)

---

## Required Folder Structure

```
hamal-techtrend/
├── agents/
│   └── __init__.py (empty for now - other agents will populate)
├── data/
│   ├── projects.json (seed with RANGER, TrailWatch examples)
│   └── techtrend_context.md (company background, Forest Service domain)
├── outputs/
│   └── .gitkeep (ensure folder is tracked but empty)
├── tests/
│   └── .gitkeep
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
└── KEEP_IT_SIMPLE.md
```

---

## File Contents

### 1. `README.md`

```markdown
# Hamal: AI-Powered Validation Framework for TechTrend

**Version:** 0.1.0 (MVP)  
**Status:** Proof-of-Concept  
**Purpose:** Validate government AI project opportunities through autonomous agent research

***

## What is Hamal?

Hamal transforms rough agency requests into validated project specifications in 15-20 minutes. When TechTrend receives an opportunity (e.g., "Forest Service needs post-fire AI"), Hamal:

1. **Discovery Agent:** Validates the core problem (5 Whys, stakeholder mapping)
2. **Research Agent:** Finds similar government projects, competitors, failures
3. **Validation Agent:** Scores feasibility (0-50), identifies risks
4. **Similarity Agent:** Matches against TechTrend's past projects (reusable components)
5. **Architecture Agent:** Generates stack recommendation, cost estimate, timeline
6. **Synthesis Agent:** Produces Go/No-Go decision report

**Output:** Complete Design phase artifacts (research.md, validation.md, architecture.md, decision.md)

***

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure API Keys

Copy `.env.example` to `.env` and add your keys:

```bash
cp .env.example .env
# Edit .env with your API keys
```

### 3. Run Discovery Agent (Test)

```bash
python agents/discovery.py data/test_charter.txt
```

### 4. Run Full Pipeline (After all agents built)

```bash
python hamal.py run data/ranger_charter.txt
```

***

## Project Structure

- **agents/** - Individual agent implementations (discovery, research, validation, etc.)
- **data/** - TechTrend project history, domain context, test inputs
- **outputs/** - Generated reports per validation run (outputs/project-name/)
- **tests/** - Test cases for agents
- **hamal.py** - Main orchestrator CLI (built in Week 7-8)

***

## Development Philosophy

⚠️ **READ FIRST:** [KEEP_IT_SIMPLE.md](KEEP_IT_SIMPLE.md)

This is a POC to validate that agent swarms save time on TechTrend Design phases. Our goal is to test agent prompts, not build production infrastructure.

**Core principles:**
- Use single-file Python scripts, hardcoded values, JSON files for storage
- No databases, no auth, no tests, no CI/CD until we prove agents work
- Ship ugly code weekly, iterate on prompts aggressively
- Functional > perfect. Speed > elegance. Learning > scaling.

***

## Tech Stack

- **Language:** Python 3.11+
- **Orchestration:** LangGraph (multi-agent coordination)
- **LLMs:** OpenRouter (GPT-4 + Claude 3.5 + Gemini)
- **Web Search:** Tavily API
- **Storage:** Local JSON files (outputs/ directory)
- **UI (Week 8):** React + Vite + TailwindCSS

***

## Success Metrics

**MVP is successful if:**
- [ ] Saves 5+ hours per Design phase (measurable via time tracking)
- [ ] Produces 3+ insights per project that AI Lead wouldn't find manually
- [ ] Runs on 3 different TechTrend projects (RANGER, TrailWatch, 1 new)
- [ ] A2UI demonstrates real-time agent progress (not just loading spinner)

***

## Contributing

This is an internal TechTrend tool (for now). If you're a Builder on the team:

1. Read `KEEP_IT_SIMPLE.md` first
2. Each agent is a self-contained Python file
3. Test on real projects (RANGER, TrailWatch)
4. Focus on prompt quality, not infrastructure

***

## License

Internal TechTrend project. Not open source (yet).

***

**Contact:** AI Lead, TechTrend Inc.
```

---

### 2. `requirements.txt`

```txt
# Core LLM/Agent Libraries
anthropic==0.18.1
openai==1.12.0
langchain==0.1.9
langgraph==0.0.26
langchain-anthropic==0.1.4
langchain-openai==0.0.6

# Web Search
tavily-python==0.3.0

# Utilities
python-dotenv==1.0.1
click==8.1.7
pydantic==2.6.1

# Optional (for embeddings/similarity search)
sentence-transformers==2.3.1
numpy==1.26.3

# Optional (for PDF parsing if uploading charters)
pypdf2==3.0.1
```

---

### 3. `.env.example`

```bash
# LLM API Keys
ANTHROPIC_API_KEY=your_key_here
OPENAI_API_KEY=your_key_here

# Web Search API
TAVILY_API_KEY=your_key_here

# Optional: OpenRouter (unified LLM access)
OPENROUTER_API_KEY=your_key_here

# Optional: Google Cloud (Phase 2)
GOOGLE_CLOUD_PROJECT=your_project_id
GOOGLE_APPLICATION_CREDENTIALS=path/to/service-account.json
```

---

### 4. `.gitignore`

```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Environment
.env
.env.local

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# Outputs (generated reports)
outputs/*/

# OS
.DS_Store
Thumbs.db

# Logs
*.log

# Test files
test_charter.txt
```

---

### 5. `KEEP_IT_SIMPLE.md`

```markdown
# Keep It Simple: Hamal Development Manifesto

**This is a proof-of-concept, not production software.**

Our goal is to **validate that agent swarms save time**, not build enterprise-grade infrastructure. Every technical decision should optimize for **speed of learning**, not scalability, security, or elegance.

## Core Principles

### 1. **Functional > Perfect**
- Hardcode values instead of building config systems
- Use `.env` files, not secret managers
- JSON files in `/data`, not databases (until we need search)
- Print statements for debugging, not observability platforms

### 2. **Prototype-Grade Code Is Fine**
- No CI/CD pipelines (deploy manually)
- No test coverage requirements (manual testing on real projects)
- No error handling beyond try/catch (crash loudly, fix what breaks)
- No type hints or linting (unless it helps you think)

### 3. **Agents First, Infrastructure Later**
- **Spend 80% of time tuning prompts**, 20% on code structure
- If an agent isn't useful, delete it—don't optimize it
- Prove the concept with ugly code, refactor if it works

### 4. **Ship Weekly, Kill Early**
- Every Friday: Does this save time? Yes → continue. No → kill.
- If Week 2 doesn't improve on Week 1, stop and reassess
- No sunk cost fallacy: 10 hours wasted is better than 40

### 5. **No Premature Abstraction**
- Don't build "agent frameworks"—write scripts that call APIs
- Don't build "plugin systems"—copy/paste code for now
- Don't build "reusable libraries"—solve the problem in front of you

## The One-Paragraph Reminder

**Paste this at the start of every working session:**

```
This is a proof-of-concept to validate that agent swarms save time on TechTrend 
Design phases. Our goal is to test agent prompts, not build production 
infrastructure. Use single-file Python scripts, hardcoded values, JSON files 
for storage, and print() for debugging. No databases, no auth, no tests, no 
CI/CD until we prove agents work. Ship ugly code weekly, iterate on prompts 
aggressively, and kill anything that doesn't save time by Friday. 
Functional > perfect. Speed > elegance. Learning > scaling.
```

***

**Version:** 1.0  
**Use this:** Paste the one-paragraph reminder into every working session  
**Update this:** When you discover new "simple" patterns, add them here
```

---

### 6. `data/projects.json`

**Purpose:** Seed TechTrend's past project history for Similarity Agent to search

```json
[
  {
    "id": "ranger_2025",
    "name": "RANGER",
    "problem": "Post-fire recovery coordination across multiple agencies - manual consolidation of damage reports causing 40-60% delays in crew deployment",
    "agency": "USDA Forest Service",
    "stack": ["FastAPI", "React", "Vertex AI", "AlloyDB", "Cloud Run"],
    "timeline": "12 weeks",
    "cost": "$85,000",
    "outcome": "Deployed in 3 regions, 40% faster triage, FedRAMP Moderate compliant",
    "lessons": [
      "Multi-format data ingestion (PDF, Word, email) was hardest part",
      "Real-time processing not needed - 4-hour batch was acceptable",
      "Inter-agency MOA took 3 weeks (legal bottleneck)"
    ],
    "compliance": ["FedRAMP Moderate", "508 Accessibility", "PII handling"],
    "date": "2025-08"
  },
  {
    "id": "trailwatch_2025",
    "name": "TrailWatch",
    "problem": "Trail damage reporting and triage - citizens report damage via photo/GPS, AI classifies severity, auto-generates closure notices",
    "agency": "USDA Forest Service",
    "stack": ["FastAPI", "React PWA", "Vertex AI", "Cloud Storage", "Firebase"],
    "timeline": "6 weeks (MVP)",
    "cost": "$45,000",
    "outcome": "Pilot in 2 national forests, 60% reduction in manual triage time",
    "lessons": [
      "Photo classification (Gemini Vision) worked better than expected (92% accuracy)",
      "Citizen adoption required marketing push (not just technical solution)",
      "Offline-first PWA was critical for rural connectivity"
    ],
    "compliance": ["508 Accessibility", "Public-facing security"],
    "date": "2025-11"
  }
]
```

---

### 7. `data/techtrend_context.md`

**Purpose:** Provide agents with TechTrend-specific domain knowledge

```markdown
# TechTrend Context for Hamal Agents

**Purpose:** This file contains TechTrend-specific context that agents should use when validating opportunities.

***

## Company Background

**TechTrend, Inc.** is a Google Cloud Partner consultancy specializing in AI solutions for government agencies. We operate the **AI Factory** model:

- **Design Phase:** $5K, 2-3 weeks (research, scope, architecture, fixed-price proposal)
- **Build Phase:** Fixed price, 6-16 weeks (rapid prototyping, MVP-first)
- **Deploy Phase:** Customer environment (FedRAMP, on-prem, hybrid)
- **Transfer Phase:** Full code/docs/knowledge transfer (zero vendor lock-in)

**Differentiator:** We pass AI productivity gains to customers (10% of traditional cost, weeks not years)

***

## Primary Domain: USDA Forest Service

**Expertise areas:**
- Wildfire management (pre-fire prevention, active response, post-fire recovery)
- Trail maintenance and public safety
- Multi-agency coordination (Forest Service, BLM, FEMA, state agencies)
- Citizen reporting and engagement
- GIS/mapping integration (Esri ArcGIS compatibility)

**Common pain points:**
- Manual data consolidation from multiple sources (PDF, Word, email, phone)
- Slow inter-agency coordination (MOAs, data sharing agreements)
- Limited real-time processing capability (batch is more realistic)
- Budget constraints (federal procurement cycles, continuing resolutions)
- Compliance burden (FedRAMP, 508, PII/CUI handling)

***

## TechTrend's Preferred Tech Stack

**Backend:**
- **Language:** Python (FastAPI framework)
- **Database:** AlloyDB (PostgreSQL-compatible, GCP-native)
- **AI/ML:** Vertex AI (Gemini, PaLM, custom models)
- **Storage:** Cloud Storage (files, photos, documents)

**Frontend:**
- **Framework:** React (PWA for offline capability)
- **Styling:** Tailwind CSS
- **Hosting:** Cloud Run or Firebase Hosting

**Deployment:**
- **Platform:** Google Cloud Platform (primary)
- **Containers:** Docker + Cloud Run
- **Compliance:** FedRAMP Moderate via Assured Workloads
- **CI/CD:** Cloud Build (though we prefer manual for MVP)

**Why GCP:** TechTrend is a Google Cloud Partner, team is trained on GCP, customer agencies often use GCP

***

## Federal Procurement & Compliance

**Contract Vehicles:**
- GSA Schedule 70 (IT solutions)
- Ability One (if applicable)
- Direct agency contracts (existing relationships)

**Compliance Requirements (Typical):**
- **FedRAMP:** Moderate or High (depending on data sensitivity)
- **508 Accessibility:** WCAG 2.1 AA compliance for public-facing systems
- **PII/CUI:** Proper handling of Personally Identifiable Information / Controlled Unclassified Information
- **ATO:** Authority to Operate (security authorization process, 3-6 months)

**Procurement Timing:**
- **Fast:** Existing contract mod, small dollar (<$25K), pilot project
- **Slow:** New RFP, multi-agency coordination, >$250K, requires Congressional approval

***

## Historical Project Patterns

**Success factors:**
- **Clear problem definition** (not "we need AI" but "crew deployment takes 3 days when it should take 3 hours")
- **Executive sponsorship** (charter-level or CIO support)
- **Realistic timeline** (6-16 weeks for MVP, not "ASAP")
- **Batch over real-time** (4-hour latency is acceptable in most cases)
- **MVP mindset** (deploy 80% solution fast, iterate after seeing usage)

**Red flags (often lead to NO-GO):**
- **Real-time requirements** without justification (adds 2-3x complexity)
- **Multi-agency without MOA** (legal coordination takes months)
- **Vague problem statement** ("improve efficiency" without quantified metrics)
- **Technology-first thinking** ("we want to use blockchain/AI" without clear use case)
- **Budget uncertainty** ("we think we have funding but...")

***

## Competitors (Awareness)

**Large integrators:**
- Palantir (Foundry platform - $500K+/year, vendor lock-in)
- Deloitte, Accenture (traditional consulting, multi-year timelines)
- Esri (GIS-focused, strong in Forest Service but weak AI)

**TechTrend advantage:**
- Fixed-price (no hourly billing)
- Weeks not years (AI-accelerated delivery)
- No vendor lock-in (you own everything)
- GCP-native (not multi-cloud complexity)

***

## Use This Context When:

1. **Discovery Agent:** Understand agency mission, common pain points
2. **Research Agent:** Search for similar Forest Service projects, government precedents
3. **Validation Agent:** Apply TechTrend's feasibility rubric (technical, compliance, timeline, budget)
4. **Similarity Agent:** Match against RANGER, TrailWatch patterns
5. **Architecture Agent:** Default to TechTrend stack (FastAPI + React + Vertex AI)

***

**Last Updated:** January 10, 2026  
**Maintained By:** AI Lead, TechTrend Inc.
```

---

## Deliverables Checklist

After running this prompt, you should have:

- [ ] Folder structure created (agents/, data/, outputs/, tests/)
- [ ] `README.md` with project overview and quick start
- [ ] `requirements.txt` with all Python dependencies
- [ ] `.env.example` with API key placeholders
- [ ] `.gitignore` configured for Python + outputs
- [ ] `KEEP_IT_SIMPLE.md` with POC philosophy
- [ ] `data/projects.json` seeded with RANGER, TrailWatch
- [ ] `data/techtrend_context.md` with company/domain knowledge
- [ ] `agents/__init__.py` (empty, ready for other agents)

---

## Success Criteria

**This agent succeeds if:**
1. A new developer can `git clone` and run `pip install -r requirements.txt` without errors
2. `README.md` clearly explains what Hamal is and how to get started
3. `data/projects.json` contains realistic TechTrend project examples
4. `KEEP_IT_SIMPLE.md` reminds everyone this is a POC, not production code

---

## Notes

- **No code files yet** - other agents (2-6) will populate `agents/` folder
- **Simple is better** - hardcode what you can, avoid over-engineering
- **Test it** - try running `pip install -r requirements.txt` to verify dependencies resolve

---

**Ready to build? Start now. Keep it simple. Ship it ugly.**
```

***

## AGENT 2: DISCOVERY AGENT BUILDER

**Launch:** Phase 1 (No dependencies)  
**Estimated Time:** 45-60 minutes  
**Output Files:** `agents/discovery.py`

### PROMPT:

```markdown
# Agent 2: Discovery Agent Builder - Hamal Framework

**Date:** January 10, 2026  
**Project:** Hamal @ TechTrend (AI-powered validation framework for government AI projects)  
**Your Role:** Build the Problem Interrogation Agent (5 Whys methodology + autonomous context gathering)

---

## Context: What Does the Discovery Agent Do?

When TechTrend receives a vague agency request like "We need AI for post-fire recovery," the Discovery Agent:

1. **Interrogates the problem** using Socratic questioning (5 Whys)
2. **Maps stakeholders** (who feels pain? who pays? who blocks?)
3. **Quantifies pain** (frequency, severity, cost of status quo)
4. **Gathers context autonomously** (searches web for agency background, recent news, mission)
5. **Outputs validated problem statement** (core problem, stakeholders, pain severity, willingness to pay)

**Goal:** Get from vague charter → validated problem statement in 30 minutes (vs. 1-2 weeks of manual back-and-forth)

---

## Your Task

Build `agents/discovery.py` - a Python script that:

1. Takes agency charter text as input (from file or string)
2. Uses Claude API to ask 5 Socratic questions about the problem
3. Searches the web for agency context (mission, budget, recent news)
4. Generates a validated problem statement in markdown format
5. Can run standalone via CLI: `python agents/discovery.py <charter_file.txt>`

---

## Technical Requirements

### Input
- **Charter text:** Plain text file or string (email, meeting notes, PDF-extracted text)
- **Example:** "USDA Forest Service needs AI system for post-fire recovery coordination. Multiple agencies submit damage reports. Current process takes weeks. Budget: TBD. Timeline: Urgent."

### Output
- **File:** `outputs/[project-name]/problem.md`
- **Format:** Markdown with validated problem statement

### Dependencies
- `anthropic` (Claude API)
- `tavily-python` (web search)
- `python-dotenv` (load API keys)
- `click` (optional, for CLI interface)

---

## Implementation Guide

### File: `agents/discovery.py`

```python
#!/usr/bin/env python3
"""
Discovery Agent - Problem Interrogation via 5 Whys + Context Gathering

Purpose: Transform vague agency charter into validated problem statement
Method: Socratic questioning + autonomous web research
Output: problem.md (validated problem statement)
"""

import os
import anthropic
from tavily import TavilyClient
from dotenv import load_dotenv

load_dotenv()

# Initialize clients
claude = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))


def interrogate_problem(charter_text: str) -> dict:
    """
    Use 5 Whys methodology to extract core problem.
    
    Returns dict with:
    - core_problem: str
    - pain_severity: str (High/Medium/Low)
    - frequency: str
    - current_workaround: str
    - stakeholders: list
    """
    
    system_prompt = """You are a critical problem discovery agent for government AI projects.
Your job: Use Socratic questioning to get from surface request → root cause → validated problem statement.

Framework (5 Whys):
1. What specific task is painful?
2. Why is that task painful?
3. What's the consequence of that pain?
4. How often does this happen?
5. What's the current workaround?

Be direct. Ask one question at a time. Don't explain your reasoning - just ask the question.

After 5 questions, synthesize into:
- Core Problem: [one sentence, specific]
- Pain Severity: High/Medium/Low [with reasoning]
- Frequency: [X times per year/month]
- Current Workaround: [what they do today]
- Stakeholders: [who feels pain, who pays, who blocks]
- Willingness to Pay: [evidence from charter]
"""
    
    # For POC: We'll simulate the 5 questions without interactive user input
    # In production, this could be conversational via CLI or UI
    
    response = claude.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=2048,
        system=system_prompt,
        messages=[{
            "role": "user",
            "content": f"""Agency charter:

{charter_text}

Run through the 5 Whys framework and extract:
1. Core Problem (one specific sentence)
2. Pain Severity (High/Medium/Low with reasoning)
3. Frequency (how often this happens)
4. Current Workaround (what they do today)
5. Stakeholders (who feels pain, who pays, who blocks)
6. Willingness to Pay (evidence from charter)

Format as structured output, not conversational questions."""
        }]
    )
    
    # Parse Claude's response (for POC, assume structured text)
    result_text = response.content.text
    
    # Return as dict (in production, parse more carefully)
    return {
        "raw_analysis": result_text,
        "charter": charter_text
    }


def gather_context(agency_name: str, problem_domain: str) -> dict:
    """
    Search web for agency background:
    - Mission statement
    - Recent news
    - Budget info
    - Leadership
    
    Returns dict with context findings.
    """
    
    # Search queries
    queries = [
        f"{agency_name} mission statement",
        f"{agency_name} {problem_domain} recent news",
        f"{agency_name} budget 2026"
    ]
    
    context = {"findings": []}
    
    for query in queries:
        try:
            results = tavily.search(query, max_results=3)
            context["findings"].append({
                "query": query,
                "results": results.get("results", [])
            })
        except Exception as e:
            print(f"Search error for '{query}': {e}")
            context["findings"].append({
                "query": query,
                "error": str(e)
            })
    
    return context


def generate_problem_statement(interrogation: dict, context: dict) -> str:
    """
    Synthesize interrogation + context into final problem.md
    
    Uses Claude to combine findings into clean markdown.
    """
    
    system_prompt = """You are synthesizing problem discovery findings into a validated problem statement.

Output format (markdown):

# Validated Problem Statement

## Core Problem
[One sentence, specific, quantified if possible]

## Pain Severity
**Level:** High / Medium / Low
**Reasoning:** [Why this severity?]

## Frequency
[How often does this problem occur?]

## Current Workaround
[What are they doing today to cope?]

## Stakeholders
- **Pain Sufferers:** [who experiences the problem daily]
- **Budget Owner:** [who would pay to solve this]
- **Potential Blockers:** [who might resist change]

## Willingness to Pay
**Evidence:** [from charter/context - is budget approved? pilot funding? or speculative?]

## Agency Context
[Brief background on agency mission, recent initiatives related to this problem]

***

**Confidence Level:** [High/Medium/Low - based on charter clarity]
**Recommended Next Step:** [Research similar projects / Schedule stakeholder interviews / Request more detail on X]
"""
    
    response = claude.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=3000,
        system=system_prompt,
        messages=[{
            "role": "user",
            "content": f"""Synthesize these findings into a validated problem statement:

## Interrogation Results:
{interrogation['raw_analysis']}

## Agency Context from Web Search:
{context}

Generate the markdown problem statement following the template."""
        }]
    )
    
    return response.content.text


def run_discovery(charter_text: str, project_name: str) -> str:
    """
    Full discovery pipeline.
    
    Returns: path to generated problem.md
    """
    
    print("🔍 Discovery Agent: Interrogating problem...")
    interrogation = interrogate_problem(charter_text)
    
    # Extract agency name (simple heuristic for POC)
    agency_name = "USDA Forest Service" if "forest" in charter_text.lower() else "Federal Agency"
    problem_domain = "post-fire recovery" if "fire" in charter_text.lower() else "operations"
    
    print(f"🌐 Discovery Agent: Gathering context on {agency_name}...")
    context = gather_context(agency_name, problem_domain)
    
    print("📝 Discovery Agent: Generating problem statement...")
    problem_md = generate_problem_statement(interrogation, context)
    
    # Save output
    output_dir = f"outputs/{project_name}"
    os.makedirs(output_dir, exist_ok=True)
    
    output_path = f"{output_dir}/problem.md"
    with open(output_path, "w") as f:
        f.write(problem_md)
    
    print(f"✅ Discovery Agent complete: {output_path}")
    
    return output_path


# CLI Interface (for standalone testing)
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python agents/discovery.py <charter_file.txt>")
        print("\nExample:")
        print("  python agents/discovery.py data/ranger_charter.txt")
        sys.exit(1)
    
    charter_file = sys.argv[1]
    
    # Read charter
    with open(charter_file, "r") as f:
        charter = f.read()
    
    # Extract project name from filename
    project_name = os.path.basename(charter_file).replace(".txt", "").replace("_charter", "")
    
    # Run discovery
    output = run_discovery(charter, project_name)
    
    print("\n" + "="*60)
    print("DISCOVERY COMPLETE")
    print("="*60)
    print(f"Output: {output}")
    print("\nNext steps:")
    print("1. Review problem.md")
    print("2. Run Research Agent: python agents/research.py")
```

---

## Test Case: RANGER Charter

Create `data/ranger_charter.txt`:

```
USDA Forest Service - Post-Fire Recovery Coordination System

Problem: Multiple agencies (Forest Service, BLM, FEMA, state emergency management) 
submit damage assessment reports after wildfires. Reports come in different formats 
(PDF field notes, Word documents, emails, phone calls). Current process requires 
temporary staff to manually consolidate all reports before resource allocation 
decisions can be made. This consolidation takes 3-5 days, delaying crew deployment 
to affected areas.

Impact: 40-60% delays in getting crews to the right locations. Budget impact estimated 
at $2-3M per major fire event due to inefficient resource allocation.

Frequency: 15-20 major fire events per year in Pacific Northwest Region.

Current Approach: Hire temporary GS-7 staff during fire season to manually re-key 
data from all formats into a unified spreadsheet. Error-prone, slow, not scalable.

Request: AI system that can automatically consolidate damage reports from multiple 
formats and generate unified situational awareness dashboard for incident commanders.

Budget: Approved for pilot. $100K available for FY2026.

Timeline: Needed before next fire season (July 2026). Urgent priority.

Contact: Regional Fire Management Officer, Pacific Northwest Region
```

---

## Testing Instructions

1. **Set up environment:**
   ```bash
   export ANTHROPIC_API_KEY="your_key"
   export TAVILY_API_KEY="your_key"
   ```

2. **Create test charter:**
   ```bash
   # Create the ranger_charter.txt file above in data/ folder
   ```

3. **Run discovery agent:**
   ```bash
   python agents/discovery.py data/ranger_charter.txt
   ```

4. **Expected output:**
   - File created: `outputs/ranger/problem.md`
   - Contains validated problem statement with:
     - Core problem (crew deployment delays due to manual consolidation)
     - Pain severity (High - budget and mission impact)
     - Frequency (15-20 events/year)
     - Stakeholders (incident commanders, regional office, temporary staff)
     - Willingness to pay (budget approved, $100K pilot)

5. **Verify:**
   - Does `problem.md` surface insights beyond what's in the charter?
   - Does web search add useful agency context?
   - Would this save you 2+ hours vs. manual problem discovery?

---

## Success Criteria

**This agent succeeds if:**
1. Runs without errors on RANGER test case
2. Generates `problem.md` that's 80%+ usable without manual editing
3. Asks meaningful questions that lead to root cause (not just rephrasing charter)
4. Web search adds context that wasn't in original charter
5. Takes < 5 minutes to run (acceptable for POC)

---

## Notes for Implementation

- **Keep it simple:** No fancy conversation loop for POC - just analyze charter directly
- **Print statements:** Show progress (`print("🔍 Interrogating..."`) for debugging
- **Error handling:** Basic try/catch on web search (don't crash if Tavily fails)
- **Hardcode what you can:** Don't build config systems - focus on prompt quality

---

**Ready to build? Start now. Test on RANGER. Iterate prompts until problem.md is useful.**
```

***

## AGENT 3: RESEARCH AGENT BUILDER

**Launch:** Phase 1 (No dependencies)  
**Estimated Time:** 60-75 minutes  
**Output Files:** `agents/research.py`

### PROMPT:

```markdown
# Agent 3: Research Agent Builder - Hamal Framework

**Date:** January 10, 2026  
**Project:** Hamal @ TechTrend (AI-powered validation framework for government AI projects)  
**Your Role:** Build the Research & Precedent Finder Agent

---

## Context: What Does the Research Agent Do?

After Discovery Agent validates the problem, Research Agent finds:

1. **Government precedents** (similar projects at other agencies - DigitalGov, Challenge.gov, SAM.gov)
2. **Commercial competitors** (Palantir, Esri, Deloitte solutions in this space)
3. **Failure analysis** (similar projects that failed - why? lessons learned)

**Goal:** Find 5-10 relevant precedents + competitors in 15 minutes (vs. 3-5 hours manual Google search)

**Output:** `research.md` with categorized findings (government, commercial, failures) + lessons learned

---

## Your Task

Build `agents/research.py` - a Python script that:

1. Takes `problem.md` as input (from Discovery Agent)
2. Searches web for similar government projects, competitors, failures
3. Extracts lessons learned from precedents
4. Generates `research.md` with structured findings
5. Can run standalone: `python agents/research.py outputs/ranger/problem.md`

---

## Technical Requirements

### Input
- **problem.md:** Validated problem statement from Discovery Agent
- **Extracted fields:** Core problem, agency, domain keywords

### Output
- **File:** `outputs/[project-name]/research.md`
- **Format:** Markdown with categorized findings

### Dependencies
- `anthropic` (Claude for analysis)
- `tavily-python` (web search)
- `python-dotenv` (API keys)

---

## Implementation Guide

### File: `agents/research.py`

```python
#!/usr/bin/env python3
"""
Research Agent - Find Government Precedents, Competitors, Failures

Purpose: Search for similar projects to learn from
Method: Web search + LLM analysis of findings
Output: research.md (precedents, competitors, lessons learned)
"""

import os
import json
import anthropic
from tavily import TavilyClient
from dotenv import load_dotenv

load_dotenv()

claude = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))


def extract_search_keywords(problem_md: str) -> dict:
    """
    Parse problem.md to extract search keywords.
    
    Uses Claude to identify:
    - Agency name
    - Problem domain
    - Key technologies
    - Pain points (for finding similar problems)
    """
    
    response = claude.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1024,
        messages=[{
            "role": "user",
            "content": f"""Extract search keywords from this problem statement:

{problem_md}

Return JSON with:
- agency_name: str (e.g., "USDA Forest Service")
- problem_domain: str (e.g., "wildfire post-fire recovery")
- key_technologies: list (e.g., ["AI", "data consolidation", "multi-format ingestion"])
- pain_points: list (e.g., ["manual data entry", "multi-agency coordination", "delayed decisions"])

Output ONLY valid JSON, no explanation."""
        }]
    )
    
    # Parse JSON from Claude's response
    try:
        keywords = json.loads(response.content.text)
    except json.JSONDecodeError:
        # Fallback if parsing fails
        keywords = {
            "agency_name": "Federal Agency",
            "problem_domain": "operations",
            "key_technologies": ["AI"],
            "pain_points": ["efficiency"]
        }
    
    return keywords


def search_government_precedents(keywords: dict) -> list:
    """
    Search for similar government projects.
    
    Sources:
    - DigitalGov.gov (case studies)
    - Challenge.gov (prize competitions, past projects)
    - SAM.gov (contract awards)
    - GitHub (18F, USDS open source projects)
    """
    
    queries = [
        f"{keywords['problem_domain']} site:digital.gov",
        f"{keywords['problem_domain']} government AI case study",
        f"{keywords['problem_domain']} federal agency success story",
        f"{' '.join(keywords['key_technologies'])} {keywords['agency_name']}"
    ]
    
    findings = []
    
    for query in queries:
        try:
            print(f"  🔍 Searching: {query}")
            results = tavily.search(query, max_results=5)
            
            for result in results.get("results", []):
                findings.append({
                    "type": "government",
                    "title": result.get("title", ""),
                    "url": result.get("url", ""),
                    "snippet": result.get("content", "")
                })
        except Exception as e:
            print(f"  ⚠️  Search error: {e}")
    
    return findings[:10]  # Limit to top 10


def search_competitors(keywords: dict) -> list:
    """
    Search for commercial solutions in this space.
    
    Focus on:
    - Palantir, Esri, Deloitte (known gov contractors)
    - Startups in this domain
    - SaaS platforms
    """
    
    # Known competitors in gov AI space
    competitors = ["Palantir", "Esri", "Deloitte", "Accenture Federal", "Booz Allen"]
    
    queries = [
        f"{comp} {keywords['problem_domain']}" for comp in competitors[:3]
    ]
    
    # Add generic search
    queries.append(f"{keywords['problem_domain']} commercial software solution")
    
    findings = []
    
    for query in queries:
        try:
            print(f"  🔍 Searching: {query}")
            results = tavily.search(query, max_results=3)
            
            for result in results.get("results", []):
                findings.append({
                    "type": "commercial",
                    "title": result.get("title", ""),
                    "url": result.get("url", ""),
                    "snippet": result.get("content", "")
                })
        except Exception as e:
            print(f"  ⚠️  Search error: {e}")
    
    return findings[:8]  # Limit to top 8


def search_failures(keywords: dict) -> list:
    """
    Find similar projects that failed - extract lessons.
    
    Search for:
    - "failed modernization"
    - "lessons learned"
    - "post-mortem"
    """
    
    queries = [
        f"{keywords['problem_domain']} failed project lessons learned",
        f"{keywords['agency_name']} modernization failure",
        f"government AI project failure {keywords['problem_domain']}"
    ]
    
    findings = []
    
    for query in queries:
        try:
            print(f"  🔍 Searching: {query}")
            results = tavily.search(query, max_results=3)
            
            for result in results.get("results", []):
                findings.append({
                    "type": "failure",
                    "title": result.get("title", ""),
                    "url": result.get("url", ""),
                    "snippet": result.get("content", "")
                })
        except Exception as e:
            print(f"  ⚠️  Search error: {e}")
    
    return findings[:5]  # Limit to top 5


def analyze_findings(problem_md: str, precedents: list, competitors: list, failures: list) -> str:
    """
    Use Claude to synthesize findings into research.md
    
    Format:
    - Government Precedents (what worked, tech stack, outcomes)
    - Commercial Competitors (pricing, features, weaknesses)
    - Failure Patterns (why similar projects failed, lessons)
    - Recommendations (based on research)
    """
    
    system_prompt = """You are a government AI project researcher.

Synthesize search findings into a research report with these sections:

1. **Government Precedents** - List 3-5 most relevant projects with:
   - Project name, agency, year
   - Tech stack (if mentioned)
   - Outcome (deployed? pilot? failed?)
   - Key lesson (what did they learn?)

2. **Commercial Competitors** - List 2-4 vendors with:
   - Company name, product
   - Estimated pricing (if known, or "enterprise pricing")
   - Strengths (what they do well)
   - Weaknesses (gaps, cost, lock-in)

3. **Failure Patterns** - Common reasons similar projects failed:
   - Technical issues (wrong tech choice, scale problems)
   - Process issues (timeline too aggressive, wrong procurement vehicle)
   - Stakeholder issues (lack of buy-in, multi-agency coordination)

4. **Key Takeaways** - 3-5 insights from research:
   - What approaches worked best?
   - What should we avoid?
   - What's the realistic timeline/cost based on precedents?

Format in clean markdown. Be specific, cite URLs where relevant."""
    
    # Combine findings into context
    findings_text = f"""
## Government Precedents Found:
{json.dumps(precedents, indent=2)}

## Commercial Competitors Found:
{json.dumps(competitors, indent=2)}

## Failure Cases Found:
{json.dumps(failures, indent=2)}
"""
    
    response = claude.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=4000,
        system=system_prompt,
        messages=[{
            "role": "user",
            "content": f"""Original problem:

{problem_md}

***

Research findings:

{findings_text}

Synthesize into research.md following the 4-section format."""
        }]
    )
    
    return response.content.text


def run_research(problem_md_path: str) -> str:
    """
    Full research pipeline.
    
    Returns: path to generated research.md
    """
    
    # Read problem.md
    with open(problem_md_path, "r") as f:
        problem_md = f.read()
    
    project_name = os.path.basename(os.path.dirname(problem_md_path))
    
    print("🔍 Research Agent: Extracting search keywords...")
    keywords = extract_search_keywords(problem_md)
    print(f"   Keywords: {keywords}")
    
    print("\n🌐 Research Agent: Searching government precedents...")
    precedents = search_government_precedents(keywords)
    print(f"   Found {len(precedents)} precedents")
    
    print("\n🏢 Research Agent: Searching commercial competitors...")
    competitors = search_competitors(keywords)
    print(f"   Found {len(competitors)} competitors")
    
    print("\n⚠️  Research Agent: Searching failure cases...")
    failures = search_failures(keywords)
    print(f"   Found {len(failures)} failure cases")
    
    print("\n📝 Research Agent: Synthesizing findings...")
    research_md = analyze_findings(problem_md, precedents, competitors, failures)
    
    # Save output
    output_path = f"outputs/{project_name}/research.md"
    with open(output_path, "w") as f:
        f.write(research_md)
    
    print(f"\n✅ Research Agent complete: {output_path}")
    
    return output_path


# CLI Interface
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python agents/research.py outputs/<project>/problem.md")
        print("\nExample:")
        print("  python agents/research.py outputs/ranger/problem.md")
        sys.exit(1)
    
    problem_path = sys.argv[1]
    
    if not os.path.exists(problem_path):
        print(f"Error: File not found: {problem_path}")
        sys.exit(1)
    
    output = run_research(problem_path)
    
    print("\n" + "="*60)
    print("RESEARCH COMPLETE")
    print("="*60)
    print(f"Output: {output}")
    print("\nNext steps:")
    print("1. Review research.md")
    print("2. Run Validation Agent: python agents/validation.py")
```

---

## Testing Instructions

1. **Prerequisites:**
   - Discovery Agent must have run first (need `outputs/ranger/problem.md`)
   - Set API keys: `ANTHROPIC_API_KEY`, `TAVILY_API_KEY`

2. **Run research:**
   ```bash
   python agents/research.py outputs/ranger/problem.md
   ```

3. **Expected output:**
   - File created: `outputs/ranger/research.md`
   - Should contain:
     - 3-5 government precedents (FEMA portal, BLM tracker, etc.)
     - 2-4 commercial competitors (Palantir, Esri)
     - Failure patterns (real-time too aggressive, MOA delays)
     - Key takeaways (batch > real-time, MVP approach)

4. **Verify:**
   - Does research.md surface projects you didn't know about?
   - Are lessons learned actionable?
   - Would this save 3+ hours vs. manual Google search?

---

## Success Criteria

**This agent succeeds if:**
1. Finds non-obvious precedents (not just first Google result)
2. Identifies realistic competitors (not generic "there are many vendors")
3. Surfaces failure patterns that inform risk mitigation
4. Runs in < 10 minutes (acceptable for POC)
5. Generates research.md that's 80%+ usable

---

**Ready to build? Focus on search query quality. Test on RANGER. Iterate until findings are useful.**
```

***

## AGENT 4: VALIDATION AGENT BUILDER

**Launch:** Phase 1 (No dependencies)  
**Estimated Time:** 60-75 minutes  
**Output Files:** `agents/validation.py`

### PROMPT:

```markdown
# Agent 4: Validation Agent Builder - Hamal Framework

**Date:** January 10, 2026  
**Project:** Hamal @ TechTrend (AI-powered validation framework for government AI projects)  
**Your Role:** Build the Feasibility Scoring & Risk Analysis Agent

---

## Context: What Does the Validation Agent Do?

After Research Agent finds precedents, Validation Agent:

1. **Scores feasibility** on 5 dimensions (0-10 each, 0-50 composite):
   - Technical Complexity
   - Compliance Burden
   - Stakeholder Alignment
   - Timeline Pressure
   - Budget Clarity

2. **Identifies riskiest assumptions** (what must be true for this to work?)
3. **Flags red flags** (similar to Humane Pin-style failure patterns)
4. **Recommends mitigation strategies** (how to de-risk)

**Goal:** Score project feasibility objectively, flag top 3 risks (vs. gut-check from AI Lead)

**Output:** `validation.md` with feasibility score, risk register, mitigation strategies

---

## Your Task

Build `agents/validation.py` - a Python script that:

1. Takes `problem.md` + `research.md` as input
2. Uses Claude to score feasibility on 5 dimensions
3. Identifies riskiest assumptions and red flags
4. Generates `validation.md` with structured risk assessment
5. Can run standalone: `python agents/validation.py outputs/ranger/`

---

## Technical Requirements

### Input
- **problem.md:** Validated problem statement
- **research.md:** Government precedents, competitors, failures

### Output
- **File:** `outputs/[project-name]/validation.md`
- **Format:** Markdown with feasibility score, risk register

### Dependencies
- `anthropic` (Claude for scoring/analysis)
- `python-dotenv` (API keys)

---

## Implementation Guide

### File: `agents/validation.py`

```python
#!/usr/bin/env python3
"""
Validation Agent - Feasibility Scoring & Risk Analysis

Purpose: Score project on 5 dimensions, identify risks
Method: LLM-based scoring with domain-specific rubric
Output: validation.md (feasibility score, risk register)
"""

import os
import json
import anthropic
from dotenv import load_dotenv

load_dotenv()

claude = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))


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
    
    response = claude.messages.create(
        model="claude-3-5-sonnet-20241022",
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
        scores = json.loads(response.content.text)
    except json.JSONDecodeError:
        # Fallback if parsing fails
        print("⚠️  Warning: Could not parse scoring JSON, using defaults")
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
    
    response = claude.messages.create(
        model="claude-3-5-sonnet-20241022",
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
        risks = json.loads(response.content.text)
    except json.JSONDecodeError:
        print("⚠️  Warning: Could not parse risk JSON, using defaults")
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
    
    response = claude.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=3000,
        system=system_prompt,
        messages=[{
            "role": "user",
            "content": f"""Generate validation report:

## Scores:
{json.dumps(scores, indent=2)}

## Risks:
{json.dumps(risks, indent=2)}

Follow the markdown format template."""
        }]
    )
    
    return response.content.text


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
    
    with open(problem_path, "r") as f:
        problem_md = f.read()
    
    with open(research_path, "r") as f:
        research_md = f.read()
    
    project_name = os.path.basename(project_dir)
    
    print("📊 Validation Agent: Scoring feasibility...")
    scores = score_feasibility(problem_md, research_md)
    print(f"   Composite Score: {scores.get('composite_score', 'N/A')}/50")
    
    print("\n⚠️  Validation Agent: Analyzing risks...")
    risks = analyze_risks(problem_md, research_md, scores)
    print(f"   Identified {len(risks.get('riskiest_assumptions', []))} key assumptions")
    
    print("\n📝 Validation Agent: Generating report...")
    validation_md = generate_validation_report(scores, risks)
    
    # Save output
    output_path = os.path.join(project_dir, "validation.md")
    with open(output_path, "w") as f:
        f.write(validation_md)
    
    print(f"\n✅ Validation Agent complete: {output_path}")
    
    return output_path


# CLI Interface
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python agents/validation.py outputs/<project>/")
        print("\nExample:")
        print("  python agents/validation.py outputs/ranger/")
        sys.exit(1)
    
    project_dir = sys.argv.rstrip("/")[1]
    
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
```

---

## Testing Instructions

1. **Prerequisites:**
   - `outputs/ranger/problem.md` (from Discovery Agent)
   - `outputs/ranger/research.md` (from Research Agent)

2. **Run validation:**
   ```bash
   python agents/validation.py outputs/ranger/
   ```

3. **Expected output:**
   - File created: `outputs/ranger/validation.md`
   - Should contain:
     - Feasibility score (likely 32-38/50 for RANGER = CONDITIONAL GO)
     - Dimension breakdown (Technical 7/10, Compliance 6/10, etc.)
     - Top 3 riskiest assumptions (MOA approval, OCR accuracy)
     - Red flags (real-time expectations, inter-agency coordination)
     - Mitigation strategies (prototype first, technical spike)

4. **Verify:**
   - Does scoring match your intuition about RANGER's feasibility?
   - Are identified risks actually the biggest concerns?
   - Are mitigation strategies actionable?

---

## Success Criteria

**This agent succeeds if:**
1. Feasibility scoring is defensible (AI Lead agrees with 80%+ of assessments)
2. Identifies risks that AI Lead might have missed
3. Mitigation strategies are specific and actionable
4. Runs in < 5 minutes (acceptable for POC)
5. Generates validation.md that's 80%+ usable

---

**Ready to build? Focus on scoring rubric accuracy. Test on RANGER. Iterate until scores feel right.**
```

***

# PHASE 2: INTEGRATION AGENTS (LAUNCH SEQUENTIALLY AFTER PHASE 1)

***

## AGENT 5: ARCHITECTURE AGENT BUILDER

**Launch:** Phase 2 (DEPENDS ON AGENT 1 - needs `data/projects.json`)  
**Estimated Time:** 75-90 minutes  
**Output Files:** `agents/architecture.py`

### PROMPT:

```markdown
# Agent 5: Architecture Agent Builder - Hamal Framework

**Date:** January 10, 2026  
**Project:** Hamal @ TechTrend (AI-powered validation framework for government AI projects)  
**Your Role:** Build the Stack Recommendation & Cost Estimation Agent

---

## Context: What Does the Architecture Agent Do?

After Validation Agent scores feasibility, Architecture Agent:

1. **Finds similar TechTrend projects** (searches `data/projects.json` for reusable patterns)
2. **Recommends tech stack** (TechTrend defaults + project-specific adjustments)
3. **Estimates costs** (GCP runtime + dev hours based on complexity)
4. **Builds timeline** (6/12/16 week breakdown with milestones)
5. **Identifies reusable components** (from similar projects)

**Goal:** Generate buildable architecture + cost estimate (vs. 4-6 hours manual architecture design)

**Output:** `architecture.md` with stack, costs, timeline, reusable components

---

## Your Task

Build `agents/architecture.py` - a Python script that:

1. Takes `problem.md`, `validation.md`, and `data/projects.json` as input
2. Searches `projects.json` for similar TechTrend projects (semantic similarity)
3. Uses Claude to recommend stack based on TechTrend defaults + project needs
4. Estimates costs (GCP runtime + dev hours)
5. Generates timeline breakdown (6/12/16 weeks)
6. Can run standalone: `python agents/architecture.py outputs/ranger/`

---

## Technical Requirements

### Input
- **problem.md:** Validated problem
- **validation.md:** Feasibility scores
- **data/projects.json:** TechTrend project history

### Output
- **File:** `outputs/[project-name]/architecture.md`
- **Format:** Markdown with stack, costs, timeline

### Dependencies
- `anthropic` (Claude for recommendations)
- `sentence-transformers` (embeddings for similarity search)
- `numpy` (cosine similarity)
- `python-dotenv` (API keys)

---

## Implementation Guide

### File: `agents/architecture.py`

```python
#!/usr/bin/env python3
"""
Architecture Agent - Stack Recommendation & Cost Estimation

Purpose: Generate buildable architecture based on similar TechTrend projects
Method: Similarity search + LLM-based stack recommendation
Output: architecture.md (stack, costs, timeline, reusable components)
"""

import os
import json
import anthropic
import numpy as np
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv

load_dotenv()

claude = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

# Load embedding model (for similarity search)
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')


def load_project_history() -> list:
    """Load TechTrend project history from data/projects.json"""
    with open("data/projects.json", "r") as f:
        return json.load(f)


def find_similar_projects(problem_md: str, project_history: list) -> list:
    """
    Find similar TechTrend projects using semantic similarity.
    
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
    - TechTrend defaults (FastAPI, React, Vertex AI, AlloyDB)
    - Project-specific needs (from problem/validation)
    - Similar project patterns
    
    Returns dict with stack recommendation + reasoning.
    """
    
    system_prompt = """You are TechTrend's technical architect.

**TechTrend's Preferred Stack:**
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
    
    response = claude.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=3000,
        system=system_prompt,
        messages=[{
            "role": "user",
            "content": f"""Recommend tech stack for this project:

## Problem:
{problem_md}

## Validation:
{validation_md}

## Similar TechTrend Projects:
{similar_projects_text}

Return JSON with stack recommendation + reusable components."""
        }]
    )
    
    try:
        stack = json.loads(response.content[0].text)
    except json.JSONDecodeError:
        print("⚠️  Warning: Could not parse stack JSON")
        stack = {"backend": {"framework": "FastAPI"}}
    
    return stack


def estimate_costs(stack: dict, validation_scores: dict) -> dict:
    """
    Estimate costs:
    - GCP runtime (compute, storage, AI APIs)
    - Dev hours (based on complexity from validation)
    
    Returns dict with cost breakdown.
    """
    
    system_prompt = """You are estimating project costs for TechTrend.

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
    
    response = claude.messages.create(
        model="claude-3-5-sonnet-20241022",
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
        costs = json.loads(response.content[0].text)
    except json.JSONDecodeError:
        print("⚠️  Warning: Could not parse cost JSON")
        costs = {"total_project_cost": 80000, "timeline_weeks": 12}
    
    return costs


def build_timeline(complexity_scores: dict, timeline_weeks: int) -> list:
    """
    Generate week-by-week timeline with milestones.
    
    Returns list of milestones.
    """
    
    system_prompt = """You are creating a project timeline.

**Standard TechTrend phases:**
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
    
    response = claude.messages.create(
        model="claude-3-5-sonnet-20241022",
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
        timeline = json.loads(response.content[0].text)
        return timeline.get("milestones", [])
    except json.JSONDecodeError:
        print("⚠️  Warning: Could not parse timeline JSON")
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
    
    response = claude.messages.create(
        model="claude-3-5-sonnet-20241022",
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
    
    return response.content[0].text


def run_architecture(project_dir: str) -> str:
    """
    Full architecture pipeline.
    
    Returns: path to generated architecture.md
    """
    
    # Read inputs
    problem_path = os.path.join(project_dir, "problem.md")
    validation_path = os.path.join(project_dir, "validation.md")
    
    with open(problem_path, "r") as f:
        problem_md = f.read()
    
    with open(validation_path, "r") as f:
        validation_md = f.read()
    
    project_name = os.path.basename(project_dir)
    
    print("📚 Architecture Agent: Loading TechTrend project history...")
    project_history = load_project_history()
    
    print("🔍 Architecture Agent: Finding similar projects...")
    similar_projects = find_similar_projects(problem_md, project_history)
    print(f"   Found {len(similar_projects)} similar projects")
    for s in similar_projects:
        print(f"     - {s['project']['name']} (similarity: {s['similarity']:.2f})")
    
    print("\n🏗️  Architecture Agent: Recommending stack...")
    # Extract validation scores (parse from validation_md - simplified for POC)
    validation_scores = {"technical_complexity": {"score": 7}}  # Default
    stack = recommend_stack(problem_md, validation_md, similar_projects)
    
    print("\n💰 Architecture Agent: Estimating costs...")
    costs = estimate_costs(stack, validation_scores)
    print(f"   Estimated: ${costs.get('total_project_cost', 'N/A')} ({costs.get('timeline_weeks', 'N/A')} weeks)")
    
    print("\n📅 Architecture Agent: Building timeline...")
    timeline = build_timeline(validation_scores, costs.get('timeline_weeks', 12))
    
    print("\n📝 Architecture Agent: Generating report...")
    architecture_md = generate_architecture_report(stack, costs, timeline, similar_projects)
    
    # Save output
    output_path = os.path.join(project_dir, "architecture.md")
    with open(output_path, "w") as f:
        f.write(architecture_md)
    
    print(f"\n✅ Architecture Agent complete: {output_path}")
    
    return output_path


# CLI Interface
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python agents/architecture.py outputs/<project>/")
        print("\nExample:")
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
    
    print("\n" + "="*60)
    print("ARCHITECTURE COMPLETE")
    print("="*60)
    print(f"Output: {output}")
```

***

## AGENT 6: ORCHESTRATOR & CLI BUILDER

**Launch:** Phase 2 (DEPENDS ON AGENTS 2-5)  
**Estimated Time:** 90-120 minutes  
**Output Files:** `hamal.py`, `orchestrator.py`

### PROMPT:

```markdown
# Agent 6: Orchestrator & CLI Builder - Hamal Framework

**Date:** January 10, 2026  
**Project:** Hamal @ TechTrend (AI-powered validation framework)  
**Your Role:** Build main orchestration engine + CLI interface

---

## Context: What Does the Orchestrator Do?

The Orchestrator coordinates all agents in sequence:

1. Discovery Agent → problem.md
2. Research Agent → research.md
3. Validation Agent → validation.md
4. Architecture Agent → architecture.md
5. (Future) Synthesis Agent → decision.md

**Provides:**
- CLI commands (`hamal run`, `hamal discover`, etc.)
- State management (track agent progress)
- Error handling (retry failed agents)
- Output aggregation (combine all reports)

---

## Your Task

Build `hamal.py` - main CLI orchestrator that:

1. Accepts charter input (file or text)
2. Runs agents in sequence
3. Tracks progress in JSON state file
4. Handles errors gracefully
5. Outputs final reports to `outputs/[project-name]/`

---

## Implementation Guide

### File: `hamal.py`

```python
#!/usr/bin/env python3
"""
Hamal - AI-Powered Validation Framework for TechTrend

Main orchestrator: Runs agents in sequence, tracks state, generates reports.
"""

import os
import sys
import json
import click
from datetime import datetime

# Import agents
sys.path.append(os.path.dirname(__file__))
from agents import discovery, research, validation, architecture


@click.group()
def cli():
    """Hamal - Validate government AI opportunities in 15-20 minutes"""
    pass


@cli.command()
@click.argument('charter_file', type=click.Path(exists=True))
@click.option('--project-name', default=None, help='Project name (default: from filename)')
def run(charter_file, project_name):
    """Run full validation pipeline on charter"""
    
    # Extract project name
    if not project_name:
        project_name = os.path.basename(charter_file).replace('.txt', '').replace('_charter', '')
    
    click.echo(f"\n{'='*60}")
    click.echo(f"HAMAL VALIDATION: {project_name}")
    click.echo(f"{'='*60}\n")
    
    # Create output directory
    output_dir = f"outputs/{project_name}"
    os.makedirs(output_dir, exist_ok=True)
    
    # Initialize state
    state = {
        "project_name": project_name,
        "started_at": datetime.now().isoformat(),
        "charter_file": charter_file,
        "agents": {}
    }
    
    # Read charter
    with open(charter_file, 'r') as f:
        charter_text = f.read()
    
    try:
        # 1. Discovery Agent
        click.echo("🔍 Running Discovery Agent...")
        state["agents"]["discovery"] = {"status": "running", "started_at": datetime.now().isoformat()}
        save_state(state, output_dir)
        
        problem_path = discovery.run_discovery(charter_text, project_name)
        state["agents"]["discovery"] = {
            "status": "complete",
            "output": problem_path,
            "completed_at": datetime.now().isoformat()
        }
        save_state(state, output_dir)
        click.echo("✅ Discovery complete\n")
        
        # 2. Research Agent
        click.echo("🌐 Running Research Agent...")
        state["agents"]["research"] = {"status": "running", "started_at": datetime.now().isoformat()}
        save_state(state, output_dir)
        
        research_path = research.run_research(problem_path)
        state["agents"]["research"] = {
            "status": "complete",
            "output": research_path,
            "completed_at": datetime.now().isoformat()
        }
        save_state(state, output_dir)
        click.echo("✅ Research complete\n")
        
        # 3. Validation Agent
        click.echo("📊 Running Validation Agent...")
        state["agents"]["validation"] = {"status": "running", "started_at": datetime.now().isoformat()}
        save_state(state, output_dir)
        
        validation_path = validation.run_validation(output_dir)
        state["agents"]["validation"] = {
            "status": "complete",
            "output": validation_path,
            "completed_at": datetime.now().isoformat()
        }
        save_state(state, output_dir)
        click.echo("✅ Validation complete\n")
        
        # 4. Architecture Agent
        click.echo("🏗️  Running Architecture Agent...")
        state["agents"]["architecture"] = {"status": "running", "started_at": datetime.now().isoformat()}
        save_state(state, output_dir)
        
        architecture_path = architecture.run_architecture(output_dir)
        state["agents"]["architecture"] = {
            "status": "complete",
            "output": architecture_path,
            "completed_at": datetime.now().isoformat()
        }
        save_state(state, output_dir)
        click.echo("✅ Architecture complete\n")
        
        # Mark complete
        state["status"] = "complete"
        state["completed_at"] = datetime.now().isoformat()
        save_state(state, output_dir)
        
        # Summary
        click.echo("\n" + "="*60)
        click.echo("VALIDATION COMPLETE")
        click.echo("="*60)
        click.echo(f"\nOutputs saved to: {output_dir}/")
        click.echo("\nGenerated files:")
        click.echo(f"  - problem.md")
        click.echo(f"  - research.md")
        click.echo(f"  - validation.md")
        click.echo(f"  - architecture.md")
        click.echo(f"  - state.json")
        click.echo(f"\nNext steps:")
        click.echo(f"  1. Review {output_dir}/validation.md for recommendation")
        click.echo(f"  2. Review {output_dir}/architecture.md for cost/timeline")
        click.echo(f"  3. Make Go/No-Go decision")
        
    except Exception as e:
        click.echo(f"\n❌ Error: {e}", err=True)
        state["status"] = "failed"
        state["error"] = str(e)
        save_state(state, output_dir)
        sys.exit(1)


@cli.command()
@click.argument('charter_file', type=click.Path(exists=True))
@click.option('--project-name', default=None)
def discover(charter_file, project_name):
    """Run Discovery Agent only"""
    
    if not project_name:
        project_name = os.path.basename(charter_file).replace('.txt', '').replace('_charter', '')
    
    with open(charter_file, 'r') as f:
        charter_text = f.read()
    
    click.echo(f"🔍 Running Discovery Agent on {project_name}...")
    output = discovery.run_discovery(charter_text, project_name)
    click.echo(f"✅ Output: {output}")


@cli.command()
@click.argument('problem_file', type=click.Path(exists=True))
def research(problem_file):
    """Run Research Agent on problem.md"""
    
    click.echo(f"🌐 Running Research Agent...")
    output = research.run_research(problem_file)
    click.echo(f"✅ Output: {output}")


@cli.command()
@click.argument('project_dir', type=click.Path(exists=True))
def validate(project_dir):
    """Run Validation Agent on project directory"""
    
    click.echo(f"📊 Running Validation Agent...")
    output = validation.run_validation(project_dir)
    click.echo(f"✅ Output: {output}")


@cli.command()
@click.argument('project_dir', type=click.Path(exists=True))
def architect(project_dir):
    """Run Architecture Agent on project directory"""
    
    click.echo(f"🏗️  Running Architecture Agent...")
    output = architecture.run_architecture(project_dir)
    click.echo(f"✅ Output: {output}")


@cli.command()
@click.argument('project_dir', type=click.Path(exists=True))
def status(project_dir):
    """Show validation status"""
    
    state_file = os.path.join(project_dir, "state.json")
    
    if not os.path.exists(state_file):
        click.echo(f"No state found for {project_dir}")
        return
    
    with open(state_file, 'r') as f:
        state = json.load(f)
    
    click.echo(f"\nProject: {state['project_name']}")
    click.echo(f"Status: {state.get('status', 'in progress')}")
    click.echo(f"Started: {state['started_at']}")
    
    if state.get('completed_at'):
        click.echo(f"Completed: {state['completed_at']}")
    
    click.echo("\nAgent Status:")
    for agent_name, agent_state in state.get('agents', {}).items():
        status_emoji = "✅" if agent_state['status'] == 'complete' else "🔄"
        click.echo(f"  {status_emoji} {agent_name}: {agent_state['status']}")


def save_state(state: dict, output_dir: str):
    """Save state to state.json"""
    state_file = os.path.join(output_dir, "state.json")
    with open(state_file, 'w') as f:
        json.dump(state, f, indent=2)


if __name__ == '__main__':
    cli()
```

---

### File: `agents/__init__.py`

```python
"""Hamal Agents - Import all agent modules"""

from . import discovery
from . import research
from . import validation
from . import architecture

__all__ = ['discovery', 'research', 'validation', 'architecture']
```

---

## Testing Instructions

1. **Test full pipeline:**
   ```bash
   python hamal.py run data/ranger_charter.txt
   ```

2. **Test individual agents:**
   ```bash
   python hamal.py discover data/ranger_charter.txt
   python hamal.py research outputs/ranger/problem.md
   python hamal.py validate outputs/ranger/
   python hamal.py architect outputs/ranger/
   ```

3. **Check status:**
   ```bash
   python hamal.py status outputs/ranger/
   ```

4. **Expected outputs:**
   - All 4 markdown files in `outputs/ranger/`
   - `state.json` with agent completion status
   - Clean CLI progress output

---

## Success Criteria

**This orchestrator succeeds if:**
1. Full pipeline runs without manual intervention
2. Errors are caught and logged gracefully
3. State tracking works (can resume if interrupted)
4. CLI is intuitive (`hamal run` just works)
5. Takes 15-20 minutes end-to-end

---

**Ready to build? This ties everything together. Test on RANGER.**
```

***

## AGENT 7: A2UI FRONTEND BUILDER

**Launch:** Phase 3 (DEPENDS ON AGENT 6)  
**Estimated Time:** 120-150 minutes  
**Output Files:** `ui/` folder with React app

### PROMPT:

```markdown
# Agent 7: A2UI Frontend Builder - Hamal Framework

**Date:** January 10, 2026  
**Project:** Hamal @ TechTrend (AI-powered validation framework)  
**Your Role:** Build React dashboard with real-time agent progress visualization

---

## Context: What is A2UI?

A2UI (Agentic UI) is a React dashboard that:

1. **Input screen:** Upload charter or paste text
2. **Progress screen:** Real-time agent activity stream (watch agents work)
3. **Results screen:** Display validation reports, scores, recommendations

**Design decisions** (from UX-Redesign-for-Hamal.md):
- Desktop-only (1440px+)
- Hybrid execution (can watch live or return later via URL)
- Show 5 phases with agent details on expand
- Hybrid results format (Summary tab + Reports tab + Export)

---

## Your Task

Build `ui/` React app with Vite + TailwindCSS that:

1. Provides charter input form
2. Polls `outputs/[project]/state.json` for progress
3. Displays agent activity stream in real-time
4. Renders final markdown reports
5. Supports export (download ZIP of all reports)

---

## Implementation Guide

### Setup

```bash
# Create Vite React app
npm create vite@latest ui -- --template react
cd ui
npm install

# Add dependencies
npm install tailwindcss postcss autoprefixer
npm install react-markdown
npm install lucide-react
npx tailwindcss init -p
```

---

### File: `ui/src/App.jsx`

```jsx
import { useState } from 'react'
import InputForm from './components/InputForm'
import ProgressView from './components/ProgressView'
import ResultsView from './components/ResultsView'
import './App.css'

function App() {
  const [view, setView] = useState('input') // 'input' | 'progress' | 'results'
  const [projectName, setProjectName] = useState(null)

  const handleSubmit = (name) => {
    setProjectName(name)
    setView('progress')
  }

  const handleComplete = () => {
    setView('results')
  }

  return (
    <div className="min-h-screen bg-gray-50">
      <header className="bg-white border-b border-gray-200 px-8 py-4">
        <h1 className="text-2xl font-bold text-gray-900">
          Hamal <span className="text-gray-500">@ TechTrend</span>
        </h1>
        <p className="text-sm text-gray-600">
          AI-Powered Validation Framework
        </p>
      </header>

      <main className="container mx-auto px-8 py-8">
        {view === 'input' && <InputForm onSubmit={handleSubmit} />}
        {view === 'progress' && (
          <ProgressView 
            projectName={projectName} 
            onComplete={handleComplete} 
          />
        )}
        {view === 'results' && <ResultsView projectName={projectName} />}
      </main>
    </div>
  )
}

export default App
```

---

### File: `ui/src/components/InputForm.jsx`

```jsx
import { useState } from 'react'
import { Upload, FileText } from 'lucide-react'

export default function InputForm({ onSubmit }) {
  const [projectName, setProjectName] = useState('')
  const [charterText, setCharterText] = useState('')

  const handleSubmit = async (e) => {
    e.preventDefault()
    
    // Save charter to backend (simplified for POC)
    // In reality: POST to /api/validate with charter + projectName
    
    onSubmit(projectName || 'untitled')
  }

  return (
    <div className="max-w-3xl mx-auto">
      <div className="bg-white rounded-lg shadow-sm border border-gray-200 p-8">
        <h2 className="text-2xl font-bold text-gray-900 mb-2">
          Validate Agency Opportunity
        </h2>
        <p className="text-gray-600 mb-8">
          Upload charter or paste opportunity description. Validation takes ~15-20 minutes.
        </p>

        <form onSubmit={handleSubmit} className="space-y-6">
          {/* Project Name */}
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">
              Project Name
            </label>
            <input
              type="text"
              value={projectName}
              onChange={(e) => setProjectName(e.target.value)}
              placeholder="e.g., RANGER, TrailWatch"
              className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
            />
          </div>

          {/* Charter Input */}
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">
              Opportunity Description
            </label>
            <textarea
              value={charterText}
              onChange={(e) => setCharterText(e.target.value)}
              placeholder="Paste agency charter, email, or meeting notes..."
              rows={12}
              className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent font-mono text-sm"
              required
            />
          </div>

          {/* File Upload (optional for MVP) */}
          <div className="border-2 border-dashed border-gray-300 rounded-lg p-6 text-center">
            <Upload className="mx-auto h-12 w-12 text-gray-400" />
            <p className="mt-2 text-sm text-gray-600">
              Or drag and drop charter file (PDF, Word, TXT)
            </p>
            <p className="text-xs text-gray-500 mt-1">
              Optional - coming soon
            </p>
          </div>

          {/* Submit */}
          <button
            type="submit"
            disabled={!charterText}
            className="w-full bg-blue-600 text-white py-3 px-6 rounded-lg font-medium hover:bg-blue-700 disabled:bg-gray-300 disabled:cursor-not-allowed transition-colors"
          >
            Run Validation
          </button>
        </form>
      </div>
    </div>
  )
}
```

---

### File: `ui/src/components/ProgressView.jsx`

```jsx
import { useState, useEffect } from 'react'
import { CheckCircle2, Loader2, Clock } from 'lucide-react'

export default function ProgressView({ projectName, onComplete }) {
  const [state, setState] = useState(null)
  const [elapsedTime, setElapsedTime] = useState(0)

  useEffect(() => {
    // Poll state.json every 3 seconds
    const pollInterval = setInterval(async () => {
      try {
        const response = await fetch(`/outputs/${projectName}/state.json`)
        const data = await response.json()
        setState(data)

        if (data.status === 'complete') {
          clearInterval(pollInterval)
          setTimeout(onComplete, 2000) // Delay before showing results
        }
      } catch (err) {
        console.error('Error polling state:', err)
      }
    }, 3000)

    return () => clearInterval(pollInterval)
  }, [projectName, onComplete])

  useEffect(() => {
    // Update elapsed time
    const timer = setInterval(() => {
      setElapsedTime(t => t + 1)
    }, 1000)
    return () => clearInterval(timer)
  }, [])

  const agents = state?.agents || {}
  const phases = [
    { name: 'Discovery', agent: 'discovery', description: 'Validating problem statement' },
    { name: 'Research', agent: 'research', description: 'Finding precedents & competitors' },
    { name: 'Validation', agent: 'validation', description: 'Scoring feasibility' },
    { name: 'Architecture', agent: 'architecture', description: 'Generating tech stack & costs' }
  ]

  const getPhaseStatus = (agentKey) => {
    const agent = agents[agentKey]
    if (!agent) return 'pending'
    return agent.status // 'running' | 'complete' | 'failed'
  }

  const formatTime = (seconds) => {
    const mins = Math.floor(seconds / 60)
    const secs = seconds % 60
    return `${mins}:${secs.toString().padStart(2, '0')}`
  }

  return (
    <div className="max-w-4xl mx-auto">
      {/* Header */}
      <div className="bg-white rounded-lg shadow-sm border border-gray-200 p-6 mb-6">
        <div className="flex items-center justify-between">
          <div>
            <h2 className="text-2xl font-bold text-gray-900">
              Validation in Progress
            </h2>
            <p className="text-gray-600 mt-1">
              Project: {projectName}
            </p>
          </div>
          <div className="text-right">
            <div className="flex items-center gap-2 text-gray-600">
              <Clock className="w-5 h-5" />
              <span className="text-lg font-mono">{formatTime(elapsedTime)}</span>
            </div>
            <p className="text-sm text-gray-500 mt-1">
              Est. 15-20 minutes
            </p>
          </div>
        </div>
      </div>

      {/* Progress */}
      <div className="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
        <div className="space-y-4">
          {phases.map((phase, idx) => {
            const status = getPhaseStatus(phase.agent)
            const agent = agents[phase.agent]

            return (
              <div key={phase.agent} className="flex items-start gap-4 p-4 rounded-lg border border-gray-200">
                {/* Icon */}
                <div className="flex-shrink-0 mt-1">
                  {status === 'complete' && (
                    <CheckCircle2 className="w-6 h-6 text-green-600" />
                  )}
                  {status === 'running' && (
                    <Loader2 className="w-6 h-6 text-blue-600 animate-spin" />
                  )}
                  {status === 'pending' && (
                    <Clock className="w-6 h-6 text-gray-400" />
                  )}
                </div>

                {/* Content */}
                <div className="flex-grow">
                  <div className="flex items-center justify-between">
                    <h3 className="font-semibold text-gray-900">
                      Phase {idx + 1}: {phase.name}
                    </h3>
                    <span className={`text-xs font-medium px-2 py-1 rounded-full ${
                      status === 'complete' ? 'bg-green-100 text-green-700' :
                      status === 'running' ? 'bg-blue-100 text-blue-700' :
                      'bg-gray-100 text-gray-600'
                    }`}>
                      {status}
                    </span>
                  </div>
                  <p className="text-sm text-gray-600 mt-1">
                    {phase.description}
                  </p>

                  {/* Agent output preview (if available) */}
                  {agent?.output && (
                    <p className="text-xs text-gray-500 mt-2">
                      Output: {agent.output}
                    </p>
                  )}
                </div>
              </div>
            )
          })}
        </div>
      </div>
    </div>
  )
}
```

---

### File: `ui/src/components/ResultsView.jsx`

```jsx
import { useState, useEffect } from 'react'
import ReactMarkdown from 'react-markdown'
import { FileText, Download } from 'lucide-react'

export default function ResultsView({ projectName }) {
  const [activeTab, setActiveTab] = useState('summary')
  const [reports, setReports] = useState({})

  useEffect(() => {
    // Load all markdown reports
    const loadReports = async () => {
      const files = ['problem.md', 'research.md', 'validation.md', 'architecture.md']
      const loaded = {}

      for (const file of files) {
        try {
          const response = await fetch(`/outputs/${projectName}/${file}`)
          loaded[file] = await response.text()
        } catch (err) {
          console.error(`Error loading ${file}:`, err)
        }
      }

      setReports(loaded)
    }

    loadReports()
  }, [projectName])

  const handleExport = () => {
    // Trigger download of all reports as ZIP
    // For POC: just download individual files
    alert('Export feature coming soon')
  }

  return (
    <div className="max-w-6xl mx-auto">
      {/* Header */}
      <div className="bg-white rounded-lg shadow-sm border border-gray-200 p-6 mb-6">
        <div className="flex items-center justify-between">
          <div>
            <h2 className="text-2xl font-bold text-gray-900">
              Validation Complete
            </h2>
            <p className="text-gray-600 mt-1">
              Project: {projectName}
            </p>
          </div>
          <button
            onClick={handleExport}
            className="flex items-center gap-2 px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors"
          >
            <Download className="w-4 h-4" />
            Export All Reports
          </button>
        </div>
      </div>

      {/* Tabs */}
      <div className="bg-white rounded-lg shadow-sm border border-gray-200">
        <div className="border-b border-gray-200">
          <nav className="flex gap-2 px-6">
            {['summary', 'reports', 'similar'].map(tab => (
              <button
                key={tab}
                onClick={() => setActiveTab(tab)}
                className={`px-4 py-3 font-medium text-sm border-b-2 transition-colors ${
                  activeTab === tab
                    ? 'border-blue-600 text-blue-600'
                    : 'border-transparent text-gray-600 hover:text-gray-900'
                }`}
              >
                {tab.charAt(0).toUpperCase() + tab.slice(1)}
              </button>
            ))}
          </nav>
        </div>

        <div className="p-6">
          {activeTab === 'summary' && (
            <div>
              <h3 className="text-xl font-bold text-gray-900 mb-4">
                Decision Summary
              </h3>
              <div className="bg-yellow-50 border border-yellow-200 rounded-lg p-4 mb-6">
                <p className="text-sm text-yellow-800">
                  <strong>Recommendation:</strong> CONDITIONAL GO (35/50)
                </p>
                <p className="text-xs text-yellow-700 mt-1">
                  Review validation.md for conditions before proceeding
                </p>
              </div>
              {/* Add charts/scores here */}
            </div>
          )}

          {activeTab === 'reports' && (
            <div className="space-y-8">
              {Object.entries(reports).map(([filename, content]) => (
                <div key={filename} className="border border-gray-200 rounded-lg p-6">
                  <div className="flex items-center gap-2 mb-4">
                    <FileText className="w-5 h-5 text-gray-600" />
                    <h3 className="font-semibold text-gray-900">{filename}</h3>
                  </div>
                  <div className="prose prose-sm max-w-none">
                    <ReactMarkdown>{content}</ReactMarkdown>
                  </div>
                </div>
              ))}
            </div>
          )}

          {activeTab === 'similar' && (
            <div>
              <h3 className="text-xl font-bold text-gray-900 mb-4">
                Similar TechTrend Projects
              </h3>
              <p className="text-gray-600">
                Reusable components from past projects (from architecture.md)
              </p>
            </div>
          )}
        </div>
      </div>
    </div>
  )
}
```

---

## Testing Instructions

1. **Start React dev server:**
   ```bash
   cd ui
   npm run dev
   ```

2. **Run Hamal in parallel:**
   ```bash
   # In another terminal
   python hamal.py run data/ranger_charter.txt
   ```

3. **Open UI:** `http://localhost:5173`

4. **Expected flow:**
   - Input screen → submit charter
   - Progress screen → watch agents update in real-time
   - Results screen → view all reports

5. **Verify:**
   - Agent progress updates every 3 seconds
   - Markdown reports render correctly
   - Export button appears

---

## Success Criteria

**This UI succeeds if:**
1. Non-technical users can run validation without CLI
2. Agent progress is visible (not just "loading...")
3. Markdown reports are readable
4. Can export all reports for documentation
5. Works on desktop (1440px+ viewport)

---

**Ready to build? Keep it simple. Focus on UX from the redesign doc. Test on RANGER.**
```

***

# FINAL SUMMARY

## All 7 Agents Complete!

### Launch Sequence

**Phase 1 (Launch NOW - 4 agents in parallel):**
1. Agent 1: Repo Architect (30-45 min)
2. Agent 2: Discovery Agent (45-60 min)
3. Agent 3: Research Agent (60-75 min)
4. Agent 4: Validation Agent (60-75 min)

**Phase 2 (Launch after Phase 1 completes):**
5. Agent 5: Architecture Agent (75-90 min) - *Needs data/projects.json from Agent 1*
6. Agent 6: Orchestrator & CLI (90-120 min) - *Needs all agents 2-5*

**Phase 3 (Launch after Phase 2 completes):**
7. Agent 7: A2UI Frontend (120-150 min) - *Needs hamal.py from Agent 6*

***

## Total Estimated Time

- **Phase 1:** 60-75 minutes (parallel)
- **Phase 2:** 90-120 minutes (sequential)
- **Phase 3:** 120-150 minutes (sequential)

**Total:** ~5-6 hours if run perfectly, likely 8-10 hours with iterations

***

## Next Steps

1. **Save all 7 prompts** (this entire message)
2. **Open 4 Antigravity sessions**
3. **Launch Phase 1 agents simultaneously**
4. **Wait for all to complete**
5. **Launch Phase 2 agents sequentially**
6. **Launch Phase 3 agent**
7. **Test full pipeline:** `python hamal.py run data/ranger_charter.txt`

***

**You now have complete, self-contained prompts for all 7 agents. Ready to launch!** 🚀
