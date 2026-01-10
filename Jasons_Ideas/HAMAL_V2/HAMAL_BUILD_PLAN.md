# Hamal 8-Week Build Plan
## Phased Delivery with Decision Gates

**Date:** January 10, 2026  
**Version:** 1.0  
**Approach:** Incremental MVP, validate early, iterate fast  

---

## Build Philosophy

### Principles
1. **Ship weekly MVPs** (every Friday = something demoable)
2. **Validate with real projects** (RANGER, TrailWatch, not toy examples)
3. **Agent prompts > infrastructure** (get skills right before scaling)
4. **CLI before UI** (prove agents work, then add polish)
5. **Decision gates** (kill if not working, pivot if needed)

### Success Metrics (Reminder)
- **Primary:** Time savings (10-20 hours → 2-4 hours per Design phase)
- **Secondary:** Quality (insights AI Lead wouldn't find manually), Velocity (3x more opportunities evaluated)

---

## Phase Breakdown

- **Week 1-2:** Discovery Agent (Problem Interrogation)
- **Week 3-4:** Research Agent (Web Search + Precedent Finding)
- **Week 5-6:** Validation Agent (Feasibility Scoring + Risk Analysis)
- **Week 7-8:** Architecture Agent + A2UI MVP

---

## WEEK 1-2: Discovery Agent (CLI MVP)

### Goal
**Turn agency charter → validated problem statement in 30 minutes** (vs. 1-2 weeks of back-and-forth)

### What Gets Built

#### 1. **Socratic Questioning Agent** (Week 1)
```python
# hamal/agents/discovery.py

def interrogate_problem(charter: str) -> dict:
    """
    Uses 5 Whys methodology to extract:
    - Core problem
    - Pain severity
    - Frequency
    - Current workaround
    - Stakeholders
    """
    # LangChain conversational agent
    # System prompt: "You are a critical problem analyst..."
    # 5-question loop, synthesize into problem statement
```

**Test Case:** RANGER charter  
**Success:** Outputs problem statement matching what AI Lead already knows

---

#### 2. **Autonomous Context Gathering** (Week 2)
Agent doesn't just ask questions—it researches on its own:

```python
def gather_context(agency_name: str, problem_domain: str):
    """
    Searches web for:
    - Agency mission statement
    - Recent news (budget, leadership changes)
    - Similar problems in past (e.g., "Forest Service post-fire 2023")
    """
    # Tavily API or SerpAPI for web search
    # Summarizes findings into context.md
```

**Enhancement:** Agent generates hypotheses ("Based on 2023 wildfire reports, I hypothesize the bottleneck is multi-format data consolidation. Confirm?")

---

### Deliverables (End of Week 2)
- [ ] `discovery.py` working via CLI
- [ ] Test on RANGER + TrailWatch (2 real projects)
- [ ] Output: `problem.md` with validated problem statement
- [ ] Demo to self: Does this save 2+ hours vs. manual problem discovery?

### Decision Gate
**Continue if:** Agent asks smart questions that would take AI Lead 30+ minutes to research manually  
**Pivot if:** Agent outputs are too generic (means prompts need tuning, not architecture)  
**Kill if:** No time savings after 10 hours of prompt iteration

---

## WEEK 3-4: Research Agent (Web Search + Pattern Matching)

### Goal
**Find 5-10 similar government projects + competitors in 15 minutes** (vs. 3-5 hours manual search)

### What Gets Built

#### 1. **Government Precedent Finder** (Week 3)
```python
def find_gov_precedents(problem: dict) -> list:
    """
    Searches:
    - DigitalGov case studies
    - Challenge.gov archives
    - SAM.gov contract awards
    - GitHub gov repos (18F, USDS)
    
    Returns:
    - Project name, agency, tech stack, outcome
    - Lessons learned (what worked, what failed)
    """
```

**Data sources:**
- DigitalGov.gov RSS feed
- Challenge.gov API (if available, else scraping)
- SAM.gov keyword search ("post-fire" + "AI" + "Forest Service")

---

#### 2. **Similarity Search (TechTrend Project History)** (Week 4)
```python
def find_similar_techtrend_projects(problem: dict) -> list:
    """
    Compares new problem to past projects using embeddings:
    - RANGER (multi-agent coordination)
    - TrailWatch (citizen reporting)
    - [Add as projects accumulate]
    
    Returns:
    - % similarity score
    - Reusable architecture components
    - Lessons learned
    """
```

**Storage:** JSON file for now (later: Supabase with vector search)

```json
// data/projects.json
[
  {
    "id": "ranger_2025",
    "name": "RANGER",
    "problem": "Post-fire recovery coordination",
    "stack": ["FastAPI", "Vertex AI", "AlloyDB", "React"],
    "outcome": "Deployed, 40% faster triage",
    "lessons": ["Multi-format data ingestion hardest part", "Real-time not needed"]
  }
]
```

---

### Deliverables (End of Week 4)
- [ ] `research.py` working via CLI
- [ ] Test on RANGER (should find FEMA portal, BLM tracker)
- [ ] Test on TrailWatch (should find similar citizen reporting systems)
- [ ] Output: `research.md` with precedents, competitors, reusable patterns
- [ ] Demo: Does this surface 3+ insights AI Lead didn't know?

### Decision Gate
**Continue if:** Agent finds non-obvious precedents (not just Google first page)  
**Pivot if:** Web search quality is poor (switch APIs: Tavily → Exa → Perplexity)  
**Kill if:** Manual Google search is still faster after tuning

---

## WEEK 5-6: Validation Agent (Feasibility Scoring + Risk Analysis)

### Goal
**Score project 0-50 on feasibility, flag top 3 risks** (vs. gut-check from AI Lead)

### What Gets Built

#### 1. **Feasibility Scorer** (Week 5)
```python
def score_feasibility(problem: dict, research: dict) -> dict:
    """
    Scores on 5 dimensions (0-10 each):
    1. Technical complexity
    2. Compliance burden
    3. Stakeholder alignment
    4. Timeline pressure
    5. Budget clarity
    
    Returns:
    - Composite score (0-50)
    - Dimension breakdown
    - Risk flags
    - Recommended timeline (6/12/16 weeks)
    """
```

**Scoring rubric** (embedded in system prompt):
- 0-3: High risk (red flag, likely blocker)
- 4-7: Medium risk (mitigatable with planning)
- 8-10: Low risk (favorable, proceed confidently)

---

#### 2. **Risk Analyzer** (Week 6)
```python
def analyze_risks(problem: dict, research: dict, feasibility: dict) -> list:
    """
    Identifies:
    - Riskiest assumptions (what must be true for this to work?)
    - Red flags (similar projects that failed—why?)
    - Mitigation strategies (how to de-risk)
    
    Uses research.md to find failure patterns (e.g., "BLM tracker failed—timeline was too aggressive")
    """
```

**Output format:**

**Riskiest Assumptions:**

1. **Data Sharing MOA will be approved**
   - Probability: 60% (inter-agency coordination is slow)
   - Impact: Critical (no data = no project)
   - Mitigation: Prototype with synthetic data first, validate MOA in parallel

2. **Handwriting OCR accuracy >80%**
   - Probability: 70% (Gemini OCR is good but untested on field notes)
   - Impact: High (degrades to manual if <80%)
   - Mitigation: Technical spike in Week 1—scope to typed reports if OCR fails

---

### Deliverables (End of Week 6)
- [ ] `validation.py` working via CLI
- [ ] Test on RANGER + TrailWatch + 1 new project
- [ ] Output: `validation.md` with feasibility score, risk register
- [ ] Demo: Does scoring match AI Lead's intuition? Does it flag risks AI Lead missed?

### Decision Gate
**Continue if:** Scoring is defensible (AI Lead agrees with 80%+ of assessments)  
**Pivot if:** Scoring is too pessimistic/optimistic (tune rubric)  
**Kill if:** Gut-check is more accurate than agent after calibration

---

## WEEK 7-8: Architecture Agent + A2UI MVP

### Goal
**Generate stack recommendation + cost estimate + basic UI** (show agent work in real-time)

### What Gets Built

#### 1. **Architecture Generator** (Week 7)
```python
def generate_architecture(problem, feasibility, similar_projects) -> dict:
    """
    Recommends:
    - Tech stack (based on TechTrend defaults + project requirements)
    - Deployment approach (Cloud Run, FedRAMP Moderate, etc.)
    - Cost estimate ($X-Y for 6/12/16 weeks)
    - Timeline breakdown (milestones with tasks)
    
    Uses similar_projects to fork existing architecture
    """
```

**Output:** `architecture.md` matching format from Echo architecture

---

#### 2. **A2UI MVP** (Week 8)
Simple React dashboard showing agent progress in real-time

**Screens:**
1. **Input Screen:** Upload charter (PDF/text)
2. **Progress Dashboard:** Agent activity stream + feasibility chart
3. **Results Screen:** Markdown reports (research, validation, architecture) + export buttons

**Tech:**
- React + Vite (fast dev)
- TailwindCSS (rapid styling)
- WebSocket (real-time agent updates from Python backend)
- Vercel (deploy frontend, free tier)

**Agent Activity Stream (Example):**
```
✅ Discovery Agent: Problem validated (2 min ago)
🔄 Research Agent: Found 6 similar projects (1 min ago)
🔄 Validation Agent: Scoring feasibility... (now)
⏳ Architecture Agent: Queued
```

---

### Deliverables (End of Week 8)
- [ ] `architecture.py` working via CLI
- [ ] Simple web UI deployed (Vercel)
- [ ] End-to-end test: Upload RANGER charter → see agents work → download reports
- [ ] Demo to TechTrend teammate: Can they use it without AI Lead handholding?

### Decision Gate
**Continue if:** Saves 5+ hours per project, outputs are 80%+ usable  
**Pivot if:** CLI is good but UI is half-baked (ship CLI, defer UI to Phase 2)  
**Kill if:** No time savings after 8 weeks (agents too slow, outputs too generic)

---

## Weekly Cadence (Every Week)

### Monday
- Review last week's outputs
- Test on 1 real TechTrend project
- Identify gaps in agent behavior

### Tuesday-Thursday
- Build/iterate on current week's agent
- Tune prompts based on Monday test results
- Add skills (web search, embeddings, etc.)

### Friday
- Demo to self (or teammate if available)
- Document learnings (what worked, what didn't)
- Decision: Continue, pivot, or kill?

---

## Tech Stack (Locked In for 8 Weeks)

```yaml
Language: Python 3.11+
Orchestration: LangGraph (multi-agent coordination)
LLMs: OpenRouter (GPT-4 + Claude 3.5 + Gemini)
Web Search: Tavily API (or Exa, or SerpAPI)
Storage: Local JSON files (outputs/ directory)
UI (Week 8): React + Vite + TailwindCSS
Deployment: Vercel (frontend), Local (Python backend for now)
```

**No GCP yet.** Keep it simple, prove the concept, migrate to Vertex AI in Phase 2 if validated.

---

## Risk Mitigation

### What Could Go Wrong?

| Risk | Probability | Mitigation |
|------|-------------|------------|
| **Agent outputs are too generic** | High | Tune prompts weekly, add domain-specific examples |
| **Web search APIs are expensive** | Medium | Start with free tiers (Tavily 1K req/mo), upgrade if needed |
| **8 weeks isn't enough time** | Medium | Cut UI (Week 8) if agents aren't working by Week 6 |
| **No time savings vs. manual** | Low | If true by Week 4, kill project—don't sink more time |

### Weekly Decision Gates (Kill Criteria)

- **Week 2:** If Discovery Agent doesn't ask better questions than AI Lead would manually → KILL
- **Week 4:** If Research Agent doesn't find insights beyond first page of Google → KILL
- **Week 6:** If Feasibility scoring is random/inaccurate after calibration → KILL
- **Week 8:** If total time investment (40 hours) doesn't save 10+ hours per future project → PAUSE and reassess

---

## Post-8-Week: What's Next?

### If MVP Succeeds (Saves 5+ hours per project)

**Phase 2 Options:**
1. **Team rollout:** Deploy for TechTrend Builders (add auth, collaborative features)
2. **GCP migration:** Move to Vertex AI + AlloyDB (production-ready, FedRAMP path)
3. **Client-facing:** Share validation dashboard with agencies (transparency, trust-building)
4. **LLM Council:** Add multi-model consensus (if single-model accuracy isn't sufficient)

**Timeline:** Another 8 weeks (Weeks 9-16)

---

### If MVP Fails (No time savings)

**Lessons learned:**
- Agent prompts need more domain tuning? (Extend prompt engineering phase)
- Wrong problem to solve? (Maybe Architecture generation is more valuable than Research?)
- Tech stack limitation? (Try CrewAI instead of LangGraph, or local LLMs)

**Decision:** Kill, pivot, or restart with smaller scope (e.g., just Research Agent as standalone tool)

---

## Budget Estimate (8 Weeks)

### If Solo (AI Lead building in Cursor/Claude Code)
- **Time:** 40-60 hours (5-8 hours/week)
- **LLM API costs:** $50-150 (OpenRouter, web search APIs)
- **Hosting:** $0 (Vercel free tier, local Python)
- **Total:** ~$200 (mostly time, minimal cash)

### If Partnering with Antigravity
- **Scope:** TBD based on their hourly rate/engagement model
- **Estimate:** 20-40 dev hours (if they're building UI in Week 8)
- **Cost:** Depends on GCP partnership terms

---

## Immediate Next Steps (This Weekend)

### Saturday Night (Tonight, 3 hours)
1. **Create repo structure:**
   ```
   hamal-techtrend/
   ├── agents/
   │   ├── discovery.py
   │   ├── research.py
   │   ├── validation.py
   │   └── architecture.py
   ├── data/
   │   └── projects.json
   ├── outputs/
   │   └── [project-name]/
   ├── tests/
   ├── hamal.py (CLI entry point)
   └── README.md
   ```

2. **Write `discovery.py` MVP** (use code from Architecture doc)

3. **Test on RANGER charter** (does it ask good questions?)

---

### Sunday (2 hours)
4. **Refine prompts** based on RANGER test
5. **Add context gathering** (web search for agency background)
6. **Document Week 1 learnings** (what works, what needs fixing)

---

### Monday (Decision Point)
7. **Review outputs:** Is `problem.md` better than what you'd write manually in 30 minutes?
8. **Decide:** Continue Week 2 (autonomous context gathering) OR pivot prompts OR kill

---

## Success Criteria (End of 8 Weeks)

**Hamal MVP is successful if:**
- [ ] Saves 5+ hours per Design phase (measurable via time tracking)
- [ ] Produces 3+ insights per project that AI Lead wouldn't find manually
- [ ] Runs on 3 different TechTrend projects (RANGER, TrailWatch, 1 new)
- [ ] New Builder can use outputs to draft architecture without AI Lead handholding
- [ ] A2UI demonstrates real-time agent progress (not just loading spinner)

**If 4/5 are true → Phase 2 (team rollout, GCP migration)**  
**If 2-3 are true → Pivot (focus on highest-value agent, cut the rest)**  
**If 0-1 are true → Kill (lessons learned, move on)**

---

## Questions Before You Start

1. **Are you coding solo, or partnering with Antigravity from Week 1?**
   - Solo = Start tonight with `discovery.py`
   - Antigravity = Send them these 3 docs, schedule scoping call Monday

2. **What's the next real TechTrend opportunity coming in?**
   - Use that as Week 1 test case (not RANGER, since you already know the answer)

3. **Do you have API keys ready?**
   - OpenRouter (or Anthropic + OpenAI)
   - Tavily (web search)
   - Optional: Exa, SerpAPI

4. **When do you want to demo this to your team?**
   - Week 4? Week 8? Never (personal tool only)?

---

**Version:** 1.0  
**Status:** Ready to start—awaiting greenlight  
**Contact:** AI Lead, TechTrend Inc.
