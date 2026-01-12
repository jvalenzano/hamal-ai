# Company Context for Hamal Agents

**Purpose:** This file contains company-specific context that agents should use when validating opportunities.

***

## Company Background

**[Company Name]** is a technology solutions provider specializing in AI solutions for government agencies. We operate the **AI Factory** model:

- **Design Phase:** Fixed price, 2-3 weeks (research, scope, architecture, proposal)
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

## Preferred Tech Stack

**Backend:**
- **Language:** Python (FastAPI framework)
- **Database:** PostgreSQL-compatible (Cloud SQL, AlloyDB)
- **AI/ML:** LiteLLM (supporting Anthropic, OpenAI, Vertex AI)
- **Storage:** Object Storage (S3, GCS)

**Frontend:**
- **Framework:** React (PWA for offline capability)
- **Styling:** Tailwind CSS
- **Hosting:** Containerized (Cloud Run, App Runner)

**Deployment:**
- **Platform:** Cloud Agnostic (AWS, Azure, GCP supported)
- **Containers:** Docker + Orchestrator
- **Compliance:** NIST 800-53, FedRAMP Moderate capable
- **CI/CD:** GitHub Actions / GitLab CI

**Why Generic:** We adapt to the customer's cloud environment while maintaining a consistent application architecture.

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

**Large Integrators:**
- Palantir (Foundry platform - High cost, vendor lock-in)
- Deloitte, Accenture (Traditional consulting)
- Esri (GIS-focused)

**Our Advantage:**
- Fixed-price delivery
- Weeks not years
- No vendor lock-in (customer owns code)
- Modern, open-source stack

***

## Use This Context When:

1. **Discovery Agent:** Understand agency mission, common pain points
2. **Research Agent:** Search for similar government projects
3. **Validation Agent:** Apply feasibility rubric (technical, compliance, timeline, budget)
4. **Similarity Agent:** Match against historical patterns
5. **Architecture Agent:** Default to preferred stack (FastAPI + React)

***

**Last Updated:** January 11, 2026
**Maintained By:** AI Lead
