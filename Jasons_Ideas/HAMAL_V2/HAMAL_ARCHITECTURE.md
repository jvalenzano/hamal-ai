# Hamal System Architecture
## Agent Swarm + A2UI Design

**Date:** January 10, 2026  
**Version:** 1.0  
**Status:** Technical specification for development  

---

## System Overview

Hamal is a **multi-agent research system** with **adaptive UI**. It transforms unstructured agency requests into structured validation reports through autonomous agent collaboration.

### High-Level Flow

```
┌─────────────────────────────────────────────────────────────┐
│                    USER INPUT                               │
│  "Agency wants AI for post-fire recovery coordination"     │
│  (Email, PDF, meeting notes, rough charter)                │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│               HAMAL ORCHESTRATOR                            │
│  -  Parses input                                             │
│  -  Routes to agent swarm                                    │
│  -  Manages agent coordination                               │
│  -  Streams progress to A2UI                                 │
└──────────────────────┬──────────────────────────────────────┘
                       │
         ┌─────────────┼─────────────┐
         │             │             │
         ▼             ▼             ▼
┌────────────┐  ┌────────────┐  ┌────────────┐
│  RESEARCH  │  │ VALIDATION │  │ARCHITECTURE│
│   AGENT    │  │   AGENT    │  │   AGENT    │
│            │  │            │  │            │
│ -  Web      │  │ -  Risk     │  │ -  Stack    │
│   search   │  │   analysis │  │   rec      │
│ -  Pattern  │  │ -  Problem  │  │ -  Cost     │
│   match    │  │   refine   │  │   model    │
│ -  Similar  │  │ -  Feasible │  │ -  Timeline │
│   projects │  │   score    │  │   build    │
└────────────┘  └────────────┘  └────────────┘
         │             │             │
         └─────────────┼─────────────┘
                       ▼
┌─────────────────────────────────────────────────────────────┐
│                  SYNTHESIS AGENT                            │
│  -  Combines agent outputs                                   │
│  -  Generates markdown reports                               │
│  -  Creates decision framework                               │
│  -  Produces Go/No-Go recommendation                         │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│                    OUTPUT ARTIFACTS                         │
│  ├─ research.md (competitor analysis, precedents)           │
│  ├─ validation.md (risks, assumptions, Mom Test Qs)         │
│  ├─ architecture.md (stack, costs, timeline)                │
│  ├─ decision.md (Go/No-Go with evidence)                    │
│  └─ proposal.pdf (client-ready Design phase report)         │
└─────────────────────────────────────────────────────────────┘
```

---

## Agent Swarm Design

### Agent Types & Responsibilities

#### 1. **Discovery Agent** (Problem Interrogation)
**Goal:** Get from vague agency request → validated problem statement

**Skills:**
- Socratic questioning (5 Whys methodology)
- Stakeholder mapping (who feels the pain? who pays? who blocks?)
- Pain quantification (frequency, severity, cost of status quo)
- Context gathering (agency mission, budget cycle, political landscape)

**Autonomy:**
- Searches web for agency background (mission statements, org charts, budgets)
- Finds recent news/failures related to problem space
- Generates hypotheses about root cause without asking user

**Output:**

## Validated Problem Statement
**Core Problem:** Resource allocation decisions in 72-hour post-fire 
window rely on manual consolidation of multi-format damage reports, 
causing 40-60% delays in crew deployment.

**Pain Severity:** High (budget + mission impact)
**Frequency:** 15-20 major fires/year for Region
**Current Workaround:** Temporary staff manually re-keying data
**Stakeholders:** Incident commanders (pain), Regional budget office (payer)
**Willingness to Pay:** Charter-level priority, budget approved

---

#### 2. **Research Agent** (Precedent & Competitor Analysis)
**Goal:** Find what's been tried before (government + commercial)

**Skills:**
- Web search (DigitalGov, Challenge.gov, SAM.gov, GitHub gov repos)
- Pattern recognition (similar technical problems across agencies)
- Competitive analysis (Palantir, Esri, Deloitte solutions)
- Failure analysis (why did similar projects fail? lessons learned)

**Data Sources:**
- **Government:** DigitalGov case studies, 18F blog, USDS projects, Challenge.gov archives
- **Contracts:** SAM.gov awards (search "post-fire" + "AI" + "Forest Service")
- **Commercial:** Vendor whitepapers, analyst reports (Gartner, Forrester)
- **Open Source:** GitHub (USGS, NOAA, NASA repos with similar tech)

**Output:**

## Similar Projects

### Government Precedents
1. **FEMA Damage Assessment Portal (2022)**
   - Tech: ArcGIS + custom ML for photo analysis
   - Outcome: Deployed in 6 states, 40% faster triage
   - Lesson: Multi-format ingestion was hardest part

2. **BLM Fire Resource Tracker (2021)**
   - Tech: Tableau + manual ETL
   - Outcome: Failed—too slow, abandoned after 1 season
   - Lesson: Real-time requirement killed feasibility

### Commercial Competitors
- Palantir Foundry (government edition): $500K+/year
- Esri ArcGIS Emergency Management: Strong geo, weak AI
- Everbridge CEM: Real-time alerts, no analysis layer
---

#### 3. **Validation Agent** (Risk & Feasibility Assessment)
**Goal:** Surface red flags, validate assumptions, score feasibility

**Skills:**
- Risk taxonomy (technical, compliance, stakeholder, timeline, budget)
- Assumption testing (what must be true for this to work?)
- Feasibility scoring (0-10 across 5 dimensions)
- Red flag detection (Humane Pin-style failure patterns)

**Scoring Framework:**
```python
Feasibility Score (0-50):
├─ Technical Complexity (0-10)
│  ├─ Data integration: 7/10 (multi-format, but solvable)
│  ├─ AI/ML requirements: 8/10 (NLP + classification, proven tech)
│  └─ Scale: 9/10 (batch processing, not real-time)
│
├─ Compliance Burden (0-10)
│  ├─ FedRAMP: 6/10 (Moderate boundary required)
│  ├─ PII/CUI: 5/10 (damage reports contain sensitive data)
│  └─ 508 Accessibility: 8/10 (standard dashboard, testable)
│
├─ Stakeholder Alignment (0-10)
│  ├─ Single agency: 8/10 (Forest Service lead)
│  ├─ Multi-agency coordination: 5/10 (requires MOA)
│  └─ Executive sponsorship: 9/10 (charter-level)
│
├─ Timeline Pressure (0-10)
│  ├─ Urgency: 6/10 (needed by next fire season—8 months)
│  └─ Flexibility: 7/10 (MVP approach acceptable)
│
└─ Budget Clarity (0-10)
   ├─ Approved: 8/10 (charter indicates funding)
   └─ Procurement vehicle: 7/10 (can use existing contract)

Composite Score: 35/50 (70%) → CONDITIONAL GO
```

**Output:**

## Riskiest Assumptions
1. **Data Sharing MOA:** Agencies will agree to share damage reports
   - Mitigation: Prototype with anonymized/synthetic data first
   
2. **Transcription Accuracy:** AI can parse handwritten field notes
   - Mitigation: Technical spike in Week 1—if accuracy <80%, scope to typed reports only

## Red Flags
- Similar project at BLM failed in 2021 (wrong timeline expectations)
- Real-time requirement is technically infeasible—must set expectations for batch
---

#### 4. **Similarity Agent** (Pattern Matching Across TechTrend Projects)
**Goal:** Find reusable architecture from past work

**Skills:**
- Semantic search (embeddings-based matching)
- Architecture pattern extraction (FastAPI + Vertex AI = TechTrend standard)
- Component reusability (data ingestion, API design, dashboard templates)

**Data Sources:**
- **TechTrend project history:** RANGER, TrailWatch, past proposals
- **Architecture Decision Records (ADRs):** Why we chose X over Y
- **Code repos:** Reusable components, starter templates

**Output:**

## Reusable Architecture: RANGER (85% match)

**Pattern Overlap:**
- Multi-source data ingestion → AI analysis → stakeholder dashboard
- FastAPI backend + AlloyDB + React frontend
- FedRAMP Moderate boundary (compliance docs exist)

**Reusable Components:**
- `data_ingestion_pipeline.py` (handles PDF, Word, email)
- `report_generator.py` (creates markdown summaries)
- React dashboard template (responsive, 508-compliant)

**Differences:**
- RANGER has real-time component (GCP Pub/Sub)
- This project is batch-only (simpler, cheaper)
- RANGER = inter-agency, This = intra-agency (less coordination)

**Time Savings:** Start from RANGER fork → 2-3 weeks saved
---

#### 5. **Architecture Agent** (Stack & Cost Recommendations)
**Goal:** Generate buildable technical specification

**Skills:**
- Stack recommendation (based on TechTrend standards + project requirements)
- Cost modeling (GCP runtime costs + dev hours)
- Timeline estimation (6/12/16 week breakdown with milestones)
- Risk mitigation architecture (graceful degradation, fallback strategies)

**TechTrend Stack Defaults:**
```yaml
Backend: FastAPI (Python)
Frontend: React + Tailwind CSS
Database: AlloyDB (PostgreSQL-compatible)
AI/ML: Vertex AI (Gemini, PaLM, custom models)
Deployment: Cloud Run (containerized, auto-scaling)
Storage: Cloud Storage (for files/audio/images)
Compliance: FedRAMP Moderate via Assured Workloads
```

**Output:**

## Recommended Architecture

### Stack
- **Backend:** FastAPI (async, type-safe, auto docs)
- **Frontend:** React PWA (offline-capable, mobile-friendly)
- **Database:** AlloyDB (structured data + vector search)
- **AI/ML:** Vertex AI Gemini (text analysis, classification)
- **Storage:** Cloud Storage (damage reports, photos)
- **Deployment:** Cloud Run (FedRAMP Moderate boundary)

### Cost Model (Monthly, Post-Launch)
| Component | Cost |
|-----------|------|
| Cloud Run (backend) | $50-150 |
| AlloyDB | $200-400 |
| Vertex AI (Gemini) | $100-300 (usage-based) |
| Cloud Storage | $20-50 |
| **Total Runtime** | **$370-900/mo** |

### Development Cost (Fixed Price)
- **6-week MVP:** $45,000
- **12-week Full Build:** $80,000
- **16-week with Hardening:** $110,000

### Timeline (12-Week Recommendation)
- **Weeks 1-2:** Data ingestion + ETL pipeline
- **Weeks 3-4:** AI processing (Gemini classification)
- **Weeks 5-6:** Dashboard + reporting
- **Weeks 7-8:** FedRAMP compliance (security controls)
- **Weeks 9-10:** User testing + feedback incorporation
- **Weeks 11-12:** Deployment + knowledge transfer
---

#### 6. **Synthesis Agent** (Report Generation & Decision)
**Goal:** Combine all agent outputs into coherent deliverable

**Skills:**
- Narrative generation (turn structured data → readable prose)
- Decision framework (Go/No-Go with evidence)
- Artifact creation (markdown → PDF, slide deck, proposal template)

**Output:**

## Go/No-Go Recommendation

**Decision: CONDITIONAL GO** (7.2/10 confidence)

### Why GO:
- Clear problem with quantified pain (40-60% delays, $X budget impact)
- Validated precedents exist (FEMA portal, 40% improvement)
- Technical feasibility is high (proven AI components)
- Reusable architecture from RANGER (2-3 week savings)
- Budget + timeline align with TechTrend's 12-week model

### Conditions:
1. **Data Sharing MOA** must be secured (legal + stakeholder alignment)
2. **Real-time expectation** must be reset to batch (4-hour latency acceptable)
3. **Technical spike** in Week 1 to validate handwriting OCR accuracy

### Recommended Approach:
- **12-week fixed-price engagement:** $80K
- **MVP-first:** Deploy batch processing in 6 weeks, iterate based on feedback
- **Compliance-native:** FedRAMP Moderate from Day 1 (no retrofit)

### Next Steps:
1. Schedule kickoff with agency stakeholders (validate problem statement)
2. Initiate legal review for data-sharing MOA
3. Begin Design phase ($5K, 2-3 weeks)
---

## A2UI (Agentic User Interface) Design

### Core Principle: **Show Agent Work, Not Just Results**

Traditional UI: Input form → loading spinner → static report  
A2UI: Input → **live agent progress** → **interactive insights** → exportable artifacts

### UI Components

#### 1. **Agent Activity Stream**
Real-time log of agent actions (like Perplexity's search citations, but for agent tasks)

```
┌─────────────────────────────────────────────────────┐
│ HAMAL VALIDATION IN PROGRESS                        │
├─────────────────────────────────────────────────────┤
│                                                      │
│ ✅ Discovery Agent: Problem statement validated     │
│    └─ Found 3 stakeholder groups                    │
│    └─ Pain severity: High (15-20 events/year)       │
│                                                      │
│ 🔄 Research Agent: Searching government precedents  │
│    └─ Found 4 similar projects on Challenge.gov     │
│    └─ Analyzing FEMA damage assessment portal...    │
│                                                      │
│ ⏳ Validation Agent: Queued (waiting for research)  │
│                                                      │
│ ⏳ Architecture Agent: Queued                        │
│                                                      │
└─────────────────────────────────────────────────────┘
```

#### 2. **Feasibility Dashboard** (Dynamic Charts)
Updates as Validation Agent scores dimensions

```
┌─────────────────────────────────────────────────────┐
│ FEASIBILITY SCORE: 35/50 (70%) - CONDITIONAL GO    │
├─────────────────────────────────────────────────────┤
│                                                      │
│  Technical Complexity    ████████░░  8/10           │
│  Compliance Burden       ██████░░░░  6/10           │
│  Stakeholder Alignment   ███████░░░  7/10           │
│  Timeline Pressure       ███████░░░  7/10           │
│  Budget Clarity          ████████░░  8/10           │
│                                                      │
│  [View Risk Details] [Export Report]                │
│                                                      │
└─────────────────────────────────────────────────────┘
```

#### 3. **Similar Projects Grid** (Interactive Cards)
Click to expand, see architecture details, reusable components

```
┌────────────┐  ┌────────────┐  ┌────────────┐
│ RANGER     │  │ TrailWatch │  │ FAA Mod    │
│ 85% match  │  │ 40% match  │  │ 20% match  │
├────────────┤  ├────────────┤  ├────────────┤
│ Pattern:   │  │ Pattern:   │  │ Pattern:   │
│ Multi-src  │  │ Citizen    │  │ Legacy     │
│ data → AI  │  │ reporting  │  │ migration  │
│            │  │            │  │            │
│ [View...]  │  │ [View...]  │  │ [View...]  │
└────────────┘  └────────────┘  └────────────┘
```

#### 4. **Cost Breakdown** (Interactive Timeline)
Hover over phases to see tasks, drag to adjust timeline

```
┌─────────────────────────────────────────────────────┐
│ ESTIMATED COST: $80K (12 weeks)                     │
├─────────────────────────────────────────────────────┤
│                                                      │
│  Week 1-2: Data Ingestion  ████░░░░░░░░░  $12K     │
│  Week 3-4: AI Processing   ░░░████░░░░░░  $15K     │
│  Week 5-6: Dashboard       ░░░░░░████░░░  $12K     │
│  Week 7-8: Compliance      ░░░░░░░░░████  $18K     │
│  Week 9-12: Testing+Deploy ░░░░░░░░░░███  $23K     │
│                                                      │
│  [Adjust Timeline] [Export Gantt]                   │
│                                                      │
└─────────────────────────────────────────────────────┘
```

#### 5. **Decision Matrix** (Go/No-Go Visualization)
Traffic light system with drill-down into evidence

```
┌─────────────────────────────────────────────────────┐
│ RECOMMENDATION: CONDITIONAL GO                      │
├─────────────────────────────────────────────────────┤
│                                                      │
│  ✅ Market Opportunity       Strong                 │
│  ✅ Technical Feasibility    High                   │
│  ✅ Resource Fit             Aligned                │
│  ⚠️  Stakeholder Risk        Medium (MOA required)  │
│  ⚠️  Timeline Pressure       Medium (8 mo window)   │
│                                                      │
│  [View Full Analysis] [Export Decision Report]      │
│                                                      │
└─────────────────────────────────────────────────────┘
```

---

### A2UI Reference Examples (For Wireframing)

**Recommended inspirations for design:**

1. **Perplexity Pages** ([perplexity.ai](https://www.perplexity.ai/))
   - Real-time source citation
   - Expandable research sections
   - Clean, academic aesthetic

2. **Claude Artifacts** ([claude.ai](https://claude.ai/))
   - Side-by-side chat + generated content
   - Iterative refinement UI
   - Markdown rendering

3. **v0.dev** ([v0.dev](https://v0.dev/))
   - Progressive generation (show work in progress)
   - Multiple variation display
   - One-click export

4. **Notion AI** ([notion.so](https://www.notion.so/))
   - Inline AI assistance
   - Structured output (tables, lists, headers)
   - Collaborative editing

5. **GitHub Copilot Workspace** (for agent activity stream inspiration)
   - Task breakdown visualization
   - Progress indicators
   - Context-aware suggestions

---

## Technology Stack

### Phase 0: Local Development (MVP)
**Goal:** Prove agent swarm works, iterate on prompts/skills

```yaml
Orchestration: LangGraph (Python)
  - Multi-agent coordination
  - State management
  - Human-in-the-loop checkpoints

LLMs: OpenRouter (unified API)
  - GPT-4 (reasoning, synthesis)
  - Claude 3.5 Sonnet (analysis, risk assessment)
  - Gemini 2.0 (cost-effective bulk research)

Storage: Local files
  - Markdown outputs (research.md, validation.md, etc.)
  - JSON state (agent progress, intermediate results)

UI: Simple web frontend
  - React + Vite (fast dev experience)
  - TailwindCSS (rapid styling)
  - Hosted on Vercel (free tier)

Database: Supabase (optional)
  - Store project history
  - Enable similarity search (vector embeddings)
```

### Phase 1: Production (Post-MVP, if validated)
**Goal:** Scale to team, integrate with GCP ecosystem

```yaml
Orchestration: Vertex AI Agent Builder
  - GCP-native (team familiarity)
  - Built-in observability
  - FedRAMP-ready infrastructure

Storage: AlloyDB
  - Project history (searchable)
  - Vector search (similarity detection)
  - Audit logs (compliance)

Deployment: Cloud Run
  - Containerized agents
  - Auto-scaling
  - Assured Workloads boundary

UI: React SPA
  - Hosted on Cloud Run (or Firebase Hosting)
  - Google Workspace SSO (team auth)
  - Real-time updates via WebSockets
```

---

## Agent Coordination Pattern

### Sequential with Conditional Branching

```python
# Simplified LangGraph flow

def hamal_workflow(input: AgencyRequest):
    # Phase 1: Discovery (always runs first)
    problem = DiscoveryAgent.interrogate(input)
    
    # Phase 2: Research (parallel web search)
    research_results = [
        ResearchAgent.find_gov_precedents(problem),
        ResearchAgent.find_competitors(problem),
        ResearchAgent.find_failures(problem)
    ]
    
    # Phase 3: Validation (sequential, builds on research)
    feasibility = ValidationAgent.score(problem, research_results)
    
    # Decision gate: If score < 30%, stop and recommend NO-GO
    if feasibility.score < 30:
        return DecisionAgent.no_go_report(feasibility)
    
    # Phase 4: Similarity (only if GO signal)
    similar_projects = SimilarityAgent.find_matches(problem)
    
    # Phase 5: Architecture (uses similar projects as templates)
    architecture = ArchitectureAgent.design(
        problem, 
        feasibility, 
        similar_projects
    )
    
    # Phase 6: Synthesis (final report generation)
    decision = SynthesisAgent.generate_report(
        problem,
        research_results,
        feasibility,
        similar_projects,
        architecture
    )
    
    return decision
```

---

## Data Flow & State Management

### Agent State Schema
```json
{
  "project_id": "proj_2026_ranger_validation",
  "status": "in_progress",
  "current_phase": "research",
  "agents": {
    "discovery": {
      "status": "complete",
      "output": {
        "problem_statement": "...",
        "stakeholders": [...],
        "pain_severity": "high"
      }
    },
    "research": {
      "status": "in_progress",
      "progress": "60%",
      "findings": [...]
    },
    "validation": {
      "status": "queued"
    }
  },
  "artifacts": {
    "research.md": "...",
    "validation.md": null
  },
  "ui_updates": [
    {"timestamp": "2026-01-10T14:30:00", "agent": "research", "message": "Found 4 similar projects"}
  ]
}
```

---

## Security & Compliance Considerations

### Data Handling
- **PII/CUI:** Agency requests may contain sensitive info (budget, org structure)
  - Mitigation: Sanitize before sending to external LLM APIs
  - Option: Use on-prem LLM for sensitive queries (Vertex AI private endpoints)

### Audit Trail
- **Decision logs:** Every agent action logged (for reproducibility)
- **Human approval gates:** High-risk decisions require AI Lead review before proceeding

### Access Control
- **Phase 0:** Single-user (AI Lead only)
- **Phase 1:** Team access via Google Workspace SSO (Builders can view, AI Lead approves)

---

## Extensibility & Future Features

### Phase 2 Capabilities (Post-MVP)
- **LLM Council:** Multi-model consensus on go/no-go decisions
- **Client-facing mode:** Share validation dashboard with agency stakeholders
- **Retrospective analysis:** "Why did Project X go over budget?" (learn from outcomes)
- **Proactive opportunities:** Agent monitors SAM.gov for new RFPs matching TechTrend capabilities

---

## Success Criteria for Architecture

**MVP is successful if:**
- [ ] Agent swarm runs end-to-end on 3 real projects without crashing
- [ ] A2UI updates in real-time (no 30-second load-then-done pattern)
- [ ] Generated artifacts (research.md, etc.) are 80%+ usable without manual editing
- [ ] Time savings: 10-hour manual process → 2-hour Hamal-assisted process
- [ ] New Builder can understand agent outputs without AI Lead explanation

---

**Version:** 1.0  
**Next:** Review 8-Week Build Plan for phased delivery  
**Contact:** AI Lead, TechTrend Inc.

