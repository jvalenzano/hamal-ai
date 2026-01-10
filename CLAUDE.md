# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**Hamal** is a structured agentic framework for validating business ideas before writing code. It provides a 5-phase methodology (Research → Validation → Architecture → Prototyping → Decision) to help solopreneurs make evidence-based build/don't-build decisions.

**Key Mental Model:**
- **Hamal = The Assembly Line** (the product being built)
- **Echo = The First Car** (test case to prove the framework works)

Focus on framework quality, not Echo features. Echo only serves to validate Hamal.

## Project Structure

```
HAMAL/
├── hamal-framework/          # THE FRAMEWORK (the product)
│   ├── 01-research/          # Phase 1 outputs
│   ├── 02-validation/        # Phase 2 outputs
│   ├── 03-architecture/      # Phase 3 outputs
│   ├── 04-prototyping/       # Phase 4 outputs
│   ├── 05-decision/          # Phase 5 outputs
│   └── HAMAL_FRAMEWORK.md    # Complete methodology
│
├── .agent/
│   ├── rules/                # AI agent behavior rules
│   └── workflows/            # Phase automation workflows
│
├── ventures/echo/            # Test case: Second Brain concept
├── backend/                  # FastAPI backend (deployed to Render)
├── _FOCUS.md                 # Current sprint objectives
└── NORTH_STAR.md             # Complete project vision
```

## Key Documents

- **_FOCUS.md** - Check first for current objectives
- **NORTH_STAR.md** - Complete project vision and how to resume work
- **hamal-framework/HAMAL_FRAMEWORK.md** - The validation methodology

## Development Commands

### Backend (FastAPI)
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Deployment
Backend deploys to Render via `render.yaml`. Live at hamal-api.onrender.com.

## The 5-Phase Framework Workflows

Located in `.agent/workflows/`:

| Phase | Workflow | Output Location |
|-------|----------|-----------------|
| 1. Research | `/research-idea` | `01-research/[idea]-research.md` |
| 2. Validation | `/validate-idea` | `02-validation/[idea]-validation.md` |
| 3. Architecture | `/architecture-plan` | `03-architecture/[idea]-architecture.md` |
| 4. Prototyping | `/prototype-spec` | `04-prototyping/[idea]-spec.md` |
| 5. Decision | `/go-no-go` | `05-decision/[idea]-decision.md` |

Run with: `@agent run /[workflow-name]`

## Architecture Notes

- **Backend**: FastAPI + LiteLLM + Groq for AI inference
- **Agent Rules**: `.agent/rules/` contains behavior configuration (low verbosity, proactive mode)
- **Ventures**: Each validated idea gets a folder under `ventures/` with its own backend/frontend

## Core Principles

1. **Code Last** - Writing code is the most expensive validation. Do research first.
2. **Agents First** - Use AI to simulate users and critics before building.
3. **Evidence over Intuition** - Decisions based on validation scores, not gut feel.
4. **Don't skip phases** - Each phase builds on the previous one.
