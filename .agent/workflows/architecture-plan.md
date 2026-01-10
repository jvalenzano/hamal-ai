---
description: Generates a technical architecture document and stack selection.
---
# Workflow: Architecture Plan

This workflow bridges the gap between a validated idea and a buildable spec.

## Step 1: Stack Selection
**Agent Task:** Recommend the best tech stack based on the idea's requirements (e.g., Realtime -> WebSockets/SSE, Mobile -> React Native).
**Constraint:** Default to the "Hamal Stack" (FastAPI + React + Render) unless specific needs dictate otherwise.

## Step 2: Data Model Design
**Agent Task:** Outline core entities and relationships (ER Diagram).

## Step 3: System Components
**Agent Task:** Identify necessary services (Auth, Database, AI Provider, Storage).

## Step 4: Deliverable
**Agent Task:** Create `hamal-framework/03-architecture/[idea-name]-architecture.md` containing:
1.  Tech Stack Choice & Rationale
2.  Data Schema (Lite)
3.  Component Diagram (Mermaid)
4.  External Dependencies
