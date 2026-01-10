# Echo - Architecture Phase

> **Goal:** Design feasible technical architecture for Echo MVP based on Phase 1-2 insights.

---

## Key Design Decisions (From Validation Phase)

Per Phase 2 recommendations:
1. **Software-first MVP** (phone-based capture) to de-risk hardware
2. **Architecture supports future hardware path** without rewrite
3. **Privacy-first as core constraint**, not afterthought
4. **Local-first processing** with optional cloud enhancement

---

## Recommended Tech Stack

### Backend: FastAPI (Python)

**Why FastAPI:**
- Python has best AI/ML ecosystem (Whisper, LangChain, etc.)
- FastAPI is async-native (good for audio streaming)
- Type hints + auto-generated docs accelerate development
- Easy deployment to Render, Railway, or local

**Alternative Considered:** Node.js/Express
**Why Rejected:** Python AI libraries are more mature; author has stronger Python experience

### AI/LLM Processing

| Component | Choice | Rationale |
|-----------|--------|-----------|
| **Speech-to-Text** | Whisper (local) or Groq API | Local for privacy; Groq for speed fallback |
| **Note Enhancement** | Claude 3.5 Sonnet via API | Best at structured output, context understanding |
| **Agent Framework** | None (direct API calls) | Keep simple for MVP; consider CrewAI later |

**Local Processing Priority:**
- `faster-whisper` for 4x speedup on Apple Silicon
- Whisper Medium model balances accuracy (95%+) and speed
- Can run on M1/M2/M3 Mac without cloud dependency

### Frontend: Web + PWA (React)

**Why React PWA:**
- Cross-platform from single codebase
- Web Audio API for microphone capture
- PWA enables home screen install + offline audio caching
- Can add native mobile later (React Native) if needed

**Why NOT native app first:**
- Single developer constraint
- Faster iteration on web
- iOS/Android app stores add friction

### Storage: Local Obsidian Vault Sync

**Method 1: Local Folder Sync (Recommended for MVP)**
- Echo writes `.md` files to local folder
- User configures Obsidian to include that folder in vault
- Zero API dependency; works offline
- Implementation: Node.js file watcher or Python `watchdog`

**Method 2: Obsidian Plugin (Future)**
- Build community plugin for direct integration
- More complex; requires Obsidian plugin development
- Consider post-MVP if demand exists

**Data Format:**
```yaml
# Echo Note - 2026-01-10T14:30:00
---
source: echo-capture
timestamp: 2026-01-10T14:30:00
duration_seconds: 45
confidence: 0.94
audio_file: recordings/2026-01-10_1430.webm
---

[Transcribed and enhanced content here]

#echo #voice-capture
```

---

## System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                       USER DEVICE (Phone/Mac)                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌──────────────┐    ┌─────────────┐    ┌──────────────────┐   │
│  │   Capture    │───▶│  Processing │───▶│    Storage       │   │
│  │   (Web PWA)  │    │  (Local/API)│    │  (Obsidian Vault)│   │
│  └──────────────┘    └─────────────┘    └──────────────────┘   │
│         │                   │                     │              │
│         ▼                   ▼                     ▼              │
│  • Web Audio API     • Whisper (local)     • Local folder sync  │
│  • MediaRecorder     • faster-whisper      • Markdown output    │
│  • Push-to-talk UI   • Claude API (LLM)    • Audio archive     │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼ (Optional future path)
                 ┌────────────────────────┐
                 │   External Hardware    │
                 │   (ESP32 + Mic)        │
                 │   Bluetooth/WiFi to    │
                 │   phone as relay       │
                 └────────────────────────┘
```

### Data Flow (MVP)

1. **Capture:** User opens PWA → taps button → speaks
2. **Record:** WebM/WAV audio captured via Web Audio API
3. **Upload:** Audio sent to local FastAPI backend OR processed in browser
4. **Transcribe:** Whisper (local or Groq API) produces transcript
5. **Enhance:** Claude API structures transcript, adds context
6. **Store:** Markdown file written to configured Obsidian folder
7. **Sync:** Obsidian auto-indexes new file (native behavior)

### Privacy Architecture

```
┌─────────────────────────────────────────────────────┐
│                 PRIVACY-FIRST DESIGN                 │
├─────────────────────────────────────────────────────┤
│                                                      │
│  LOCAL-ONLY MODE (Default)                          │
│  ────────────────────────                           │
│  • Audio never leaves device                        │
│  • Whisper runs locally (faster-whisper)            │
│  • Notes stored in local Obsidian vault             │
│  • No network calls except LLM enhancement          │
│                                                      │
│  ENHANCED MODE (Opt-in)                             │
│  ───────────────────────                            │
│  • Groq API for faster transcription                │
│  • Claude API for note enhancement                  │
│  • Audio deleted after processing (ephemeral)       │
│  • Transcripts never stored on cloud                │
│                                                      │
│  USER CONTROLS                                      │
│  ──────────────                                     │
│  • Toggle local-only vs enhanced mode               │
│  • Control which notes use LLM enhancement          │
│  • Audio retention period (auto-delete option)      │
│                                                      │
└─────────────────────────────────────────────────────┘
```

---

## Integration Points

### Obsidian Integration

**Contract:**
- Echo writes to: `~/Obsidian/VaultName/echo-captures/`
- File naming: `YYYY-MM-DD_HHMMSS_[title-slug].md`
- Frontmatter includes: timestamp, confidence, duration, audio link
- Tags: `#echo`, `#voice-capture`, user-configurable

**Technical Requirements:**
- Obsidian vault path configurable by user
- File system write access (handled by local app or PWA with File System Access API)
- Audio files stored alongside markdown (optional)

### Whisper Integration (Local)

**Library:** `faster-whisper` via Python
**Model:** Whisper Medium (balance of speed/accuracy)
**Input:** WebM audio blob → converted to WAV if needed
**Output:** Timestamped transcript JSON

```python
# Example integration
from faster_whisper import WhisperModel

model = WhisperModel("medium", device="auto", compute_type="int8")
segments, info = model.transcribe("audio.wav", beam_size=5)
```

### Claude API Integration

**Provider:** Anthropic Claude 3.5 Sonnet
**Purpose:** Transform raw transcript → structured note
**Prompt Template:**
```
You are a note-taking assistant. Transform this voice transcript into a clean, structured markdown note suitable for a personal knowledge management system.

Transcript:
{transcript}

Instructions:
- Remove filler words and false starts
- Identify the main topic and create a clear title
- Structure with headers if multiple topics
- Add action items as checkboxes if mentioned
- Preserve the speaker's original meaning
- Output in markdown format
```

---

## MVP Scope (6-8 Weeks)

### Week 1-2: Core Infrastructure
- [ ] FastAPI backend skeleton
- [ ] Whisper integration (faster-whisper local)
- [ ] Basic audio input endpoint
- [ ] Transcript output JSON

### Week 3-4: Note Processing
- [ ] Claude API integration for note enhancement
- [ ] Markdown output formatting
- [ ] Frontmatter template
- [ ] Local folder write logic

### Week 5-6: Web Frontend
- [ ] React PWA setup
- [ ] Web Audio capture component
- [ ] Push-to-record UI
- [ ] Settings: vault path, API keys

### Week 7-8: Integration & Polish
- [ ] Obsidian folder sync testing
- [ ] End-to-end flow validation
- [ ] Error handling + edge cases
- [ ] Basic documentation
- [ ] Deploy backend (Render)

### Out of Scope for MVP
- ❌ Hardware capture device (future phase)
- ❌ Native mobile apps (PWA is sufficient)
- ❌ Multi-user / authentication
- ❌ Obsidian plugin (folder sync is simpler)
- ❌ Always-on recording (push-to-talk only)

---

## Technical Risks & Mitigations

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Whisper local performance on non-Mac | Medium | High | Offer Groq API fallback; document hardware requirements |
| Web Audio API cross-browser issues | Low | Medium | Target Chrome/Safari; test thoroughly |
| File System Access API limited browser support | Medium | Medium | Fallback: download markdown + manual import |
| Claude API costs for heavy users | Low | Low | Cache common patterns; offer local-only mode |
| Obsidian vault path complexity (cross-platform) | Medium | Medium | Clear setup guide; detect common paths |

---

## Cost Estimates (MVP)

| Resource | Cost | Notes |
|----------|------|-------|
| **Render hosting (backend)** | $7-19/mo | Starter or Standard tier |
| **Claude API (Sonnet)** | ~$0.003/note | Minimal for personal use |
| **Groq API** | Free tier: 14,400 req/day | Sufficient for MVP testing |
| **Domain** | $12/year | Optional for MVP |
| **Total Monthly MVP** | **~$10-25/mo** | Before user growth |

---

## Feasibility Assessment

| Dimension | Score | Evidence |
|-----------|-------|----------|
| **Technical Feasibility** | 8/10 | All components are proven tech; faster-whisper well-documented |
| **Time Feasibility** | 7/10 | 8-week scope is aggressive but achievable for focused work |
| **Resource Feasibility** | 9/10 | Low cost; single developer can build |
| **Integration Feasibility** | 7/10 | Obsidian folder sync is simple; plugin would be harder |

### Key Technical Challenges (Addressed)

1. **Local Whisper Performance:**
   - Solution: faster-whisper + quantization (int8) on Apple Silicon
   - Fallback: Groq API for non-Mac users

2. **Web Audio Reliability:**
   - Solution: Well-tested libraries (Recorder.js, MediaRecorder API)
   - Progressive enhancement pattern

3. **Cross-Platform File System Access:**
   - Solution: PWA File System Access API + clear instructions
   - Fallback: Download + manual vault placement

---

## Architecture Verdict

**✅ Technically Viable**

The proposed architecture:
- Uses proven, mature technologies
- Fits 6-8 week solopreneur timeline
- Supports future hardware expansion without rewrite
- Maintains privacy-first as core principle
- Has clear fallback paths for each component

**Proceed to Phase 4: Prototyping →**

---

*Phase 3 Architecture completed: January 10, 2026*
*Informed by Phase 1 (technical challenges) and Phase 2 (de-risk via software-first strategy)*
