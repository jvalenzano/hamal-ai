# Project Structure: Google Stack Edition

**Philosophy:** Monorepo with clear separation between "The Brain" (Agents) and "The Body" (Infrastructure).

```
/echo-product-workspace
├── .incubator/                 # THE BRAIN & OS
│   ├── agents/                 # LangGraph Agent Definitions
│   │   ├── researcher/
│   │   ├── skeptic/
│   │   ├── builder/
│   │   └── council_graph.py    # Main Orchestrator Graph
│   │
│   ├── infrastructure/         # IaC (The Body)
│   │   ├── terraform/          # Google Cloud Resources
│   │   └── docker/             # Cloud Run Dockerfiles
│   │
│   ├── services/               # Microservices
│   │   └── incubator-api/      # FastAPI app (runs the Agents)
│   │
│   └── memory/                 # Vertex AI Search Configs
│       └── schema.json
│
├── ventures/                   # THE PRODUCT INSTANCES
│   └── echo/
│       ├── web-dashboard/      # React + A2UI Frontend
│       │   ├── src/
│       │   └── public/
│       └── directives/         # The Directives (Input)
│
├── _FOCUS.md                   # Anchor File
└── README.md
```

## Key Locations
*   **Agent Logic:** `.incubator/agents/`
*   **API Service:** `.incubator/services/incubator-api/`
*   **Frontend:** `ventures/echo/web-dashboard/`
*   **Cloud Config:** `.incubator/infrastructure/`
