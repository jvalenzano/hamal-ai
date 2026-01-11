# Product Specification (The "Spec")

> **This is the Source of Truth for the AI Builder.**
> Update this document with natural language rules BEFORE asking for code.

## 1. High-Level Vision
Echo is a wearable second brain that captures context (voice, ambient) and processes it into a local Obsidian vault.

## 2. Core Feature Requirements
### Capture ("3-Door System")
- [ ] **Voice:** Immediate voice transcription via Whisper.
- [ ] **Web Clip:** Browser extension/bookmarklet.
- [ ] **Desktop:** Global hotkey on Mac.

### Processing
- [ ] **The "Echo" Agent:** Analyzes new notes, tags them, and links them to existing thoughts.

### Retrieval
- [ ] **Haptic Nudge:** Wristband vibrates when a relevant "Echo" is found.

## 3. Technical Logic (Directives)
*Defines constraints for the Builder.*

- **Data Privacy:** Local-first. Data leaves the device only for inference (LLM) and returns immediately.
- **Format:** All data must be stored as clear-text Markdown.
- **Latency:** Voice capture-to-text must happen in <2s.