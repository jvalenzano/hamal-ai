# Implementation Plan: Hamal OSS (Week 1)

**Goal:** Live Prototype by Sunday Night.
**Stack:** CrewAI (Groq/Ollama) + FastAPI (Render) + React (Vercel).
**Cost:** ~$0/mo (Free Tiers).

## 1. The Strategy: "Free Forever"
We are pivoting to an Open Source stack.
*   **LLM:** Groq (Llama 3.1 70B) via LiteLLM.
*   **Agent Framework:** CrewAI (Simpler, OSS).
*   **Hosting:** Render (Backend) + Vercel (Frontend).
*   **Developer Hook:** "Run locally with Ollama".

## 2. Technical Stack
1.  **Backend:** `hamal-api`
    *   **Runtime:** Python 3.11 (FastAPI).
    *   **Agents:** `crewai` + `litellm`.
    *   **Inference:** Groq API (Production) / Ollama (Local).
    *   **Host:** Render.com (Free Tier).
2.  **Frontend:** `hamal-web`
    *   **Framework:** React (Vite + TypeScript).
    *   **Host:** Vercel (Hobby Tier).

## 3. Execution Roadmap

### Phase 1: Foundation (30 min)
*   [ ] **Git Repo:** `git init` & `gh repo create hamal-ai`.
*   [ ] **API Keys:** Get Groq API Key (Free).

### Phase 2: Backend (4h)
*   [ ] **Scaffold:** `backend/` with `requirements.txt` (`fastapi`, `crewai`, `litellm`, `uvicorn`).
*   [ ] **Logic:** `backend/main.py` using CrewAI + LiteLLM.
*   [ ] **Local Test:** `uvicorn main:app` with Ollama.
*   [ ] **Deploy:** Push to GitHub -> Trigger Render Deploy.

### Phase 3: Frontend (4h)
*   [ ] **Scaffold:** `frontend/` (Vite).
*   [ ] **UI:** Risk Score Dashboard.
*   [ ] **Integration:** `fetch('https://hamal-api.onrender.com/analyze')`.
*   [ ] **Deploy:** Push to GitHub -> Trigger Vercel Deploy.

## 4. Verification Check
*   **Success:** `curl https://hamal-api.onrender.com/analyze` returns JSON from Llama 3.
