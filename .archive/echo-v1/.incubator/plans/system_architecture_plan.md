# Master Architecture Plan: The Modular Incubator OS

## The Big Shift
We are separating the **System** (The Incubator OS) from the **Instance** (Project Echo).

*   **The Incubator OS:** The reusable framework for validating *any* idea.
*   **The Venture Instance:** The specific product being built (Echo) using the OS's tools.

## 1. Directory Structure: The "Separation of Concerns"

```text
echo-product-workspace/
├── .incubator/              # <--- THE OS (Shared Framework)
│   ├── skills/              # Reusable capabilities (e.g., "LLM Council", "Market Research")
│   │   ├── llm_council/     # A skill pod
│   │   └── web_scraper/     # A skill pod
│   ├── agents/              # The 7 Personas (SysPrompt definitions)
│   └── templates/           # Blueprints (ADR template, Spec template)
│
├── ventures/                # <--- THE VENTURES (Instances)
│   └── echo/                # "Project Echo" (Focus of this workspace)
│       ├── directives/      # Specs specific to Echo
│       ├── concepts/        # <--- FEATURE PODS (The Hybrid Model)
│       │   ├── voice_interface/
│       │   │   ├── spec.md  # "What we want"
│       │   │   ├── poc/     # "The experimentation code"
│       │   │   └── skill.yaml # "How allows the OS to run this"
│       │   └── obsidian_sync/
│       └── memory/          # Logs, Decisions, Research specific to Echo
│
└── Jasons_Ideas/            # <--- THE INBOX (Unprocessed raw ideas)
```

## 2. The Logic: "Concept Pods" (Hybrid Approach)

To develop a feature for Echo (e.g., "Voice Capture"), we create a **Concept Pod** in `ventures/echo/concepts/`.

**A Concept Pod contains:**
1.  **The Directive (`spec.md`):** English-language definition of "What" and "Why".
2.  **The Experiments (`poc/`):** Messy Python/JS code validating the idea.
3.  **The Manifest (`skill.yaml`):** Metadata that tells the Incubator OS, "I exist, and here is how to invoke me."

## 3. The Implementation Steps

### Phase 1: Migration (Refactor)
1.  Establish `.incubator/` and move global items (ADR templates, generic prompts) there.
2.  Create `ventures/echo/` and move Echo-specific content there.
3.  Refactor `prototypes/` into `ventures/echo/concepts/`.

### Phase 2: Standardization
1.  Create the `concept_pod_template` so we can programmatically generate new features.
2.  Define the `skill.yaml` schema (Input, Output, Dependencies).

### Phase 3: The "LLM Council" Test
1.  Formalize `llm_council` not as an Echo feature, but as an **Incubator Skill** (`.incubator/skills/llm_council/`).
2.  Why? Because *every* future venture needs an LLM Council. It belongs to the OS, not just Echo.
