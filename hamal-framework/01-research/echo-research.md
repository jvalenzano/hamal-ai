# Echo Research Report

> **Idea:** Echo - A hands-free Second Brain that captures voice, processes it via AI, and syncs to Obsidian.

## 1. Problem Statement
Knowledge workers effectively lose 80% of their "Shower Thoughts" and verbal interactions because capturing them requires friction (pulling out a phone, unlocking, opening an app). Existing solutions are either siloes (don't sync to the Second Brain/Obsidian) or require active manual input. The goal is "Zero Friction Capture" to "Local Markdown Storage".

## 2. Competitive Landscape

| Competitor | Value Prop | Pricing | Key Weakness vs Echo |
| :--- | :--- | :--- | :--- |
| **Limitless AI (formerly Rewind)** | Wearable "Pendant" for all-day recording. Focus on meeting summaries. | $99 Hardware + $19/mo Pro | Cloud-first approach (Privacy concern). Closed ecosystem (Hard to get data *out*). |
| **Plaud Note** | Hardware record attached to phone (MagSafe). Great for calls. | ~$159 Hardware + Sub | Hardware focused on phone calls, not ambient thought capture. Proprietary app silo. |
| **Cleft Notes** | MacOS/iOS voice-to-markdown app. | Free / $7/mo | No dedicated hardware (requires phone interaction). Good Obsidian integration but manual trigger. |
| **Otter.ai** | Enterprise meeting transcription. | Free / $10/mo | Meeting focused, not personal thought capture. No direct Obsidian sync. |
| **AudioPen** | Voice-to-text summarization web app. | Freemium | Web-based friction. Good summarization, but requires active UI interaction. |

**Echo's Niche:** The gap is **Hardware-based Trigger** (Zero Friction) + **Local-First Output** (Obsidian/Markdown). Limitless is the closest hardware competitor but strikes a "Closed Garden" posture.

## 3. Market Headwinds & Tailwinds
*   **Tailwind (Strong):** **"Second Brain" Market Growth.** The Knowledge Management market is projected to reach $32B by 2030 (CAGR 18.6%).
*   **Tailwind (Middle):** **AI Wearable Normalized.** Devices like Ray-Ban Meta and Humane Pin (despite failures) have normalized the concept of wearable AI.
*   **Headwind (Critical):** **Privacy Fatigue.** "Always-on" listening is a massive barrier. Solutions must heavily emphasize *Local* or *Explicit Consent* modes.
*   **Headwind:** **Battery Physics.** Continuous on-device audio processing drains batteries rapidly.

## 4. Technical Feasibility & Challenges
*   **Privacy:** Biggest hurdle. Users reject cloud-uploading of 24/7 audio.
    *   *Mitigation:* Local-first processing (Whisper on device) or strictly ephemeral cloud processing (delete after process).
*   **Battery:** Always-on listening is a power killer.
    *   *Mitigation:* VAD (Voice Activity Detection) hardware wake-word or a Physical "Push-to-Talk" button (Echo's likely MVP path).
*   **Hallucination:** AI creating false memories.
    *   *Mitigation:* Retain original audio snippet linked to the text (like Limitless/Glean).

## 5. "Why Now?"
*   **Local AI Models:** Whisper Small/Distil run efficiently on edge devices/phones now.
*   **Obsidian Ecology:** The plugin ecosystem is mature enough to accept external webhooks (or local file changes).
*   **Hardware commoditization:** ESP32 chips with mics are cheap ($5-10) for a prototype.

## 6. Initial Feasibility Rating
**MEDIUM-HIGH**.
*   **Software side:** High feasibility (Whisper API + Obsidian Plugin).
*   **Hardware side:** Medium feasibility (Custom wearable is hard, but "Phone as mic" MVP is easy).
