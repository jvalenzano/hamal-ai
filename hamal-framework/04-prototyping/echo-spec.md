# Echo - Prototyping / MVP Specification

> **Goal:** Define detailed MVP specification with user stories, acceptance criteria, and implementation plan.

---

## MVP Vision Statement

**Echo MVP:** A web-based voice capture app that records spoken thoughts, transcribes them locally, enhances them with AI, and syncs as markdown files to an Obsidian vault.

**Target User:** Obsidian power users who want frictionless voice-to-vault capture.

**Core Value Proposition:** Capture voice → Get structured notes in your Obsidian vault, with privacy-first local processing.

---

## User Stories (MVP)

### Epic 1: Voice Capture

#### User Story 1.1: Start Recording
**As a** user,  
**I want to** press a single button to start capturing audio,  
**So that** I can record my thoughts with minimal friction.

**Acceptance Criteria:**
- [ ] Single button initiates audio recording
- [ ] Visual indicator shows recording is active (e.g., red dot, pulsing animation)
- [ ] Audio captured via Web Audio API / MediaRecorder
- [ ] Works in Chrome and Safari (mobile + desktop)

**Priority:** P0 (Critical)

---

#### User Story 1.2: Stop Recording
**As a** user,  
**I want to** stop recording by pressing the button again or after a maximum duration,  
**So that** recordings have reasonable length limits.

**Acceptance Criteria:**
- [ ] Single button press stops recording
- [ ] Auto-stop after 5 minutes (configurable)
- [ ] Recording duration displayed during capture
- [ ] Audio blob ready for processing after stop

**Priority:** P0 (Critical)

---

#### User Story 1.3: Audio Feedback
**As a** user,  
**I want to** see and hear confirmation that my recording was captured successfully,  
**So that** I have confidence the system is working.

**Acceptance Criteria:**
- [ ] Visual confirmation after recording stops (checkmark, toast notification)
- [ ] Optional audio feedback (subtle chime)
- [ ] Processing status shown (e.g., "Transcribing...", "Enhancing...", "Saved!")

**Priority:** P1 (Important)

---

### Epic 2: AI Processing

#### User Story 2.1: Transcription
**As a** user,  
**I want** my audio to be transcribed accurately,  
**So that** I get text from my spoken words.

**Acceptance Criteria:**
- [ ] Audio transcribed using Whisper (local or API)
- [ ] Transcription accuracy >90% for clear speech
- [ ] Processing time <30 seconds for 1-minute recording
- [ ] Multi-language support (using Whisper's capabilities)

**Priority:** P0 (Critical)

---

#### User Story 2.2: Note Enhancement
**As a** user,  
**I want** my transcript to be cleaned up and structured,  
**So that** the resulting note is useful without manual editing.

**Acceptance Criteria:**
- [ ] Filler words removed (um, uh, like)
- [ ] False starts cleaned up
- [ ] Coherent title generated from content
- [ ] Structure added (headers, bullets) when appropriate
- [ ] Action items converted to checkboxes

**Priority:** P1 (Important)

---

#### User Story 2.3: Optional Enhancement
**As a** privacy-conscious user,  
**I want to** choose whether to use cloud AI enhancement,  
**So that** I control when my data leaves my device.

**Acceptance Criteria:**
- [ ] Toggle in settings: "Local only" vs "Enhanced (uses Claude API)"
- [ ] Local-only mode produces raw transcript + basic cleanup
- [ ] Enhanced mode uses Claude for smarter structuring
- [ ] Clear indication of which mode is active

**Priority:** P1 (Important)

---

### Epic 3: Obsidian Sync

#### User Story 3.1: Save to Vault
**As an** Obsidian user,  
**I want** my processed notes to appear in my vault automatically,  
**So that** I don't need to manually import files.

**Acceptance Criteria:**
- [ ] Note saved as `.md` file to configured folder
- [ ] Filename format: `YYYY-MM-DD_HHMMSS_[title-slug].md`
- [ ] Obsidian sees file immediately (watches folder)
- [ ] File contains proper frontmatter (YAML)

**Priority:** P0 (Critical)

---

#### User Story 3.2: Configure Vault Path
**As a** user,  
**I want to** specify where my Obsidian vault is located,  
**So that** Echo saves files to the correct place.

**Acceptance Criteria:**
- [ ] Settings page with vault path input
- [ ] Folder picker (if File System Access API available)
- [ ] Fallback: display path for manual entry
- [ ] Validation: confirm path is writable

**Priority:** P0 (Critical)

---

#### User Story 3.3: Note Format
**As an** Obsidian user,  
**I want** notes formatted with proper frontmatter and tags,  
**So that** they integrate with my existing workflow.

**Acceptance Criteria:**
- [ ] Frontmatter includes: timestamp, source, duration, confidence
- [ ] Default tags: `#echo`, `#voice-capture`
- [ ] User-configurable additional tags
- [ ] Body content is clean markdown

**Example Output:**
```yaml
---
title: "Idea for Echo marketing"
source: echo-capture
timestamp: 2026-01-10T14:30:00
duration: 45
confidence: 0.94
tags: [echo, voice-capture]
---

# Idea for Echo marketing

Marketing angle: focus on "shower thoughts" preservation...
```

**Priority:** P1 (Important)

---

### Epic 4: Configuration

#### User Story 4.1: API Keys
**As a** user,  
**I want to** enter my API keys for Claude and optionally Groq,  
**So that** the enhanced features work with my accounts.

**Acceptance Criteria:**
- [ ] Settings page for API key entry
- [ ] Keys stored securely (local storage with warning, or backend)
- [ ] Test button to validate key
- [ ] Clear error messages if key invalid

**Priority:** P1 (Important)

---

#### User Story 4.2: Processing Mode
**As a** user,  
**I want to** choose between local processing and API processing,  
**So that** I can balance speed vs privacy.

**Acceptance Criteria:**
- [ ] Toggle: "Local (Whisper)" vs "Cloud (Groq)"
- [ ] Local mode requires no external calls for transcription
- [ ] Cloud mode is faster but sends audio to Groq
- [ ] Clear privacy implications displayed

**Priority:** P2 (Nice to have for MVP)

---

## Wireframes / UI Flow

### Main Capture Screen

```
┌─────────────────────────────────────────┐
│  Echo                    ⚙️             │
│                                          │
│                                          │
│                                          │
│           ┌───────────────┐              │
│           │               │              │
│           │    ● REC      │              │
│           │   00:00:00    │              │
│           │               │              │
│           └───────────────┘              │
│                                          │
│                                          │
│         [  🎙️  Start Recording  ]       │
│                                          │
│  Last capture: 2 min ago                │
│  └── "Meeting notes about Q2 goals"     │
│                                          │
└─────────────────────────────────────────┘
```

### Recording Active State

```
┌─────────────────────────────────────────┐
│  Echo                    ⚙️             │
│                                          │
│           ┌───────────────┐              │
│           │  ●●●●●●●●●●   │  ← Waveform  │
│           │   🔴 REC      │              │
│           │   00:01:23    │              │
│           │               │              │
│           └───────────────┘              │
│                                          │
│         [  ⏹️  Stop Recording  ]        │
│                                          │
│  Max: 5:00 remaining                     │
│                                          │
└─────────────────────────────────────────┘
```

### Processing State

```
┌─────────────────────────────────────────┐
│  Echo                    ⚙️             │
│                                          │
│           ┌───────────────┐              │
│           │               │              │
│           │  ⏳ Processing │              │
│           │               │              │
│           └───────────────┘              │
│                                          │
│  Step 1/3: Transcribing... ✓            │
│  Step 2/3: Enhancing...    ⏳            │
│  Step 3/3: Saving to vault...           │
│                                          │
└─────────────────────────────────────────┘
```

### Settings Screen

```
┌─────────────────────────────────────────┐
│  ← Settings                              │
│                                          │
│  OBSIDIAN VAULT                          │
│  ┌─────────────────────────────────────┐│
│  │ /Users/me/Obsidian/Vault/echo/     ││
│  └─────────────────────────────────────┘│
│  [📁 Browse] or enter path manually     │
│                                          │
│  ─────────────────────────────────────  │
│                                          │
│  PROCESSING MODE                         │
│  ○ Local only (Whisper on device)       │
│  ● Enhanced (Local + Claude API)        │
│                                          │
│  ─────────────────────────────────────  │
│                                          │
│  API KEYS                                │
│  Claude: ●●●●●●●●●●●● [Test] ✓          │
│  Groq (optional): Not set               │
│                                          │
│  ─────────────────────────────────────  │
│                                          │
│  DEFAULT TAGS                            │
│  [#echo] [#voice-capture] [+]           │
│                                          │
│  [Save Settings]                         │
│                                          │
└─────────────────────────────────────────┘
```

---

## API Specification

### Backend Endpoints

```
POST /api/capture
  Description: Upload audio for processing
  Input: 
    - audio_blob: binary (WebM/WAV)
    - mode: "local" | "enhanced"
  Output: 
    {
      "capture_id": "abc123",
      "status": "processing"
    }

GET /api/capture/{capture_id}
  Description: Get processing status/result
  Output: 
    {
      "capture_id": "abc123",
      "status": "complete" | "processing" | "error",
      "transcript": "...",
      "enhanced_note": "...",
      "confidence": 0.94,
      "duration_seconds": 45
    }

POST /api/save
  Description: Save note to filesystem
  Input:
    - capture_id: string
    - vault_path: string
    - tags: string[]
  Output:
    {
      "success": true,
      "file_path": "/path/to/note.md"
    }

POST /api/settings/validate
  Description: Validate API key
  Input:
    - provider: "claude" | "groq"
    - api_key: string
  Output:
    {
      "valid": true | false,
      "error": "..." (if invalid)
    }
```

---

## Implementation Phases

### Phase A: Backend Core (Week 1-2)
- [ ] FastAPI project setup
- [ ] Whisper integration (faster-whisper)
- [ ] Audio upload endpoint
- [ ] Basic transcription endpoint
- [ ] Local file write capability
- [ ] Unit tests for core functions

### Phase B: AI Enhancement (Week 3-4)
- [ ] Claude API integration
- [ ] Prompt engineering for note enhancement
- [ ] Mode switching (local vs enhanced)
- [ ] Error handling for API failures
- [ ] Async processing queue

### Phase C: Frontend PWA (Week 5-6)
- [ ] React PWA scaffold
- [ ] Web Audio recording component
- [ ] Recording UI (start/stop/status)
- [ ] Settings page
- [ ] File System Access API integration
- [ ] Offline storage for captures

### Phase D: Integration & Polish (Week 7-8)
- [ ] End-to-end flow testing
- [ ] Cross-browser testing (Chrome, Safari, Firefox)
- [ ] Error states and edge cases
- [ ] Loading states and animations
- [ ] Documentation (README, setup guide)
- [ ] Deploy backend to Render
- [ ] PWA hosting (Vercel or static)

---

## Dependencies & Blockers

### External Dependencies
| Dependency | Status | Risk |
|------------|--------|------|
| Anthropic Claude API | Available | Low - stable, well-documented |
| Groq API (optional) | Available | Low - free tier sufficient |
| faster-whisper | Available | Low - mature library |
| Web Audio API | Browser-native | Low - widely supported |

### Potential Blockers
| Blocker | Mitigation |
|---------|------------|
| File System Access API limited in Safari | Download fallback with instructions |
| Whisper performance on non-Mac | Groq API fallback |
| Cross-origin audio issues | Backend handles audio processing |

---

## Success Metrics

### MVP Launch Criteria
- [ ] User can capture voice in <3 button taps
- [ ] Note appears in Obsidian vault within 60 seconds
- [ ] Transcription accuracy >85% for clear speech
- [ ] Works on Chrome (desktop + mobile) and Safari
- [ ] Zero critical bugs in happy path

### Post-MVP Validation Metrics
- **Engagement:** User records 5+ captures in first week
- **Retention:** User returns 3+ times after first capture
- **Quality:** User edits <20% of generated notes
- **NPS:** Net Promoter Score >50 (would recommend)

---

## Out of Scope (Explicitly)

For MVP, the following are NOT included:
- ❌ Hardware capture device
- ❌ Native iOS/Android apps
- ❌ Multi-user / authentication
- ❌ Obsidian plugin (folder sync sufficient)
- ❌ Always-on / continuous recording
- ❌ Real-time transcription display
- ❌ Note editing within Echo
- ❌ Search / history browsing

These may be considered for future phases if MVP proves valuable.

---

*Phase 4 Prototyping completed: January 10, 2026*
*Informed by Phase 3 Architecture (tech stack, scope)*
