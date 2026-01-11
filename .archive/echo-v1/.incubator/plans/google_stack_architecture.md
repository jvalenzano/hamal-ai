# Architecture Plan: The Google Stack (v2.0)
> **Goal:** "Keep it simple and complex under the hood."
> **Stack:** Vertex AI Agents + Vertex AI Search + Cloud Run + Firebase.

## 1. High-Level Topology

```mermaid
graph TD
    User((Founder)) -->|UI Interaction| A2UI[A2UI Dashboard\n(React + Firebase)]
    A2UI -->|JSON Request| CloudRun[Cloud Run Service\n(Orchestrator)]
    
    subgraph "The Incubator OS (Google Cloud)"
        CloudRun -->|Orchestrate| LangGraph[LangGraph Agents]
        
        subgraph "The Council (Agents)"
            Researcher[Researcher Agent]
            Skeptic[Skeptic Agent]
            Builder[Builder Agent]
        end
        
        LangGraph -->|Invoke| Researcher
        LangGraph -->|Invoke| Skeptic
        
        Researcher -->|Search Context| VertexRAG[Vertex AI Search\n(RAG Store)]
        Skeptic -->|Search Context| VertexRAG
        
        Researcher -->|Generate| JSON[Structured JSON]
        Skeptic -->|Generate| JSON
    end
    
    JSON -->|Stream| A2UI
    CloudRun -->|Persist| Firestore[Firestore DB]
    CloudScheduler[Cloud Scheduler] -->|Trigger Weekly| CloudRun
```

## 2. Component Decisions (The "Three Answers")

### A. The Brain: Programmatic Agents (LangGraph)
*   **Why:** We need guaranteed JSON outputs for the Dashboard, not chat text.
*   **Implementation:** Python-based LangGraph running on Cloud Run.
*   **Model:** Gemini 1.5 Pro with `response_schema` (Structured Output).

### B. The Memory: Vertex AI Search (RAG)
*   **Why:** NotebookLM has no API. Vertex Search is the API-first equivalent.
*   **Implementation:**
    *   **Corpus:** Founder uploads PDFs/Docs -> Google Drive -> Vertex Search Index.
    *   **Retrieval:** Agents use `GoogleVertexAISearchRetriever` tool.

### C. The Body: Cloud Run + Firebase
*   **Why:** Scale to zero, 99.6% gross margin, native Google integration.
*   **Implementation:**
    *   **Frontend:** React (hosting on Firebase Hosting or Vercel).
    *   **Backend:** Python FastAPI (LangGraph) on Cloud Run.
    *   **DB:** Firestore (Real-time updates for Dashboard).

## 3. The Data Flow
1.  **Input:** Founder types "I want an AI meetings app" into Dashboard.
2.  **Processing:**
    *   `POST /api/incubate` -> Cloud Run.
    *   LangGraph spins up 7 parallel nodes.
    *   Each node calls Vertex Gemini with JSON Schema.
3.  **Output:**
    *   Agents return JSON: `{ "score": 85, "risks": [...] }`.
    *   Frontend renders `<RiskCard data={response.risks} />` (A2UI Pattern).
