import os

PROJECT_ROOT = "echo-product-workspace"

def create_file(relative_path, content):
    full_path = os.path.join(PROJECT_ROOT, relative_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ Created: {relative_path}")

# --- 1. CRITIQUE PROMPTS ---
content_critique = """# ECHO PROJECT: MULTI-LLM CRITIQUE FRAMEWORK
## Ready-to-Use Vetting Prompts

## PROMPT 1: THE "SKEPTICAL VC"
Target LLM: Claude 3.5 Sonnet or GPT-4o

> "Act as a battle-hardened Venture Capitalist (Partner level at Sequoia) who specializes in consumer hardware and AI.
> **The Pitch:** 'Echo' is a wearable second brain (earbud + haptic wristband) that uses autonomous AI to connect humans, not distract them. It listens to your voice and ambient conversations, processes them via a local-first Obsidian Vault, and uses an autonomous Claude Agent to surface 'echoes'—connections to your past thoughts or friends—via haptic nudges. It is hands-free, works on a '3-door capture' system (Voice, Web Clip, Mac Hotkey), and is built on an open-source, self-healing agentic architecture (Antigravity/Claude Code).
> **Your Task:** Tear this pitch apart.
> 1. The 'Who Cares' Test: Why is this not just a feature of Apple Airpods?
> 2. The Hardware Trap: How do they solve battery life with always-on Whisper?
> 3. The Moat: If Ray-Ban Meta glasses add 'memory', does Echo die?
> 4. The User Friction: Will normal people wear a wristband just for haptics?
> Deliver a brutal, honest memo on why you would PASS today."

## PROMPT 2: THE "HARDWARE REALITY CHECK"
Target LLM: Gemini Advanced

> "Act as a Senior Hardware Engineer. Your job is to validate the specs of 'Echo'.
> **The Specs:** Discrete earbud + Haptic/E-ink Wristband. Always-on voice transcription (Whisper) + Local syncing. Battery Goal: 12-16 hours. Compute: Ambiq Atomiq or Arm Cortex-M85.
> **Your Task:** Perform a feasibility analysis.
> 1. Power Budget: Can always-on mic + BLE run 12h on 50mAh?
> 2. Latency: Can we get haptic feedback in <200ms?
> 3. Thermal Constraints: Will the earbud get hot?
> 4. Supply Chain: Are chips available for solopreneurs?
> Output a 'Green/Yellow/Red' feasibility score."

## PROMPT 3: THE "MARKET SYNTHESIZER"
Target LLM: Llama 3 or Claude

> "You are the 'Catalyst'—a strategic co-founder.
> **Task:** Synthesize the VC and Hardware critiques.
> 1. Identify the 'Killer Assumption': What kills the company if false?
> 2. The Pivot Path: Is there a software-only MVP?
> 3. The Verdict: Give me a probability score (0-100%) of success."
"""

# --- 2. STRUCTURE ---
content_structure = """# ECHO PROJECT BLUEPRINT

## 1. NAMING CONCEPTS
**The Winner: ECHO** (One syllable. Represents thoughts "echoing" back.)
**Contenders:** Soma, Nexus, Vibe, Loop, Flux, Chord, Pulse.

## 2. GITHUB REPOSITORY STRUCTURE
```text
echo-product-workspace/
├── .agentic/
│   ├── agents.yaml             # 7 expert personas
│   └── prompts/
├── directives/
│   ├── product_spec.md
│   └── architecture_decisions/
├── research/
│   ├── market_validation/
│   └── hardware_specs/
├── prototypes/
│   ├── voice_capture_poc/
│   └── obsidian_plugin/
├── inspiration/
│   └── brand_narrative.md
└── logs/
    ├── week_01_log.md
    └── decisions.md