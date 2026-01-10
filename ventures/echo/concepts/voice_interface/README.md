# Voice Capture POC (Experiment)

## Goal
Validate that we can capture audio on a Mac and transcribe it using OpenAI Whisper (or local equivalent) with acceptable latency.

## Requirements
*   **Input:** Microphone audio.
*   **Process:** Detect silence -> Stop recording -> Send to API/Model.
*   **Output:** Text string printed to console.
*   **Success Metric:** < 2 seconds from silence to text.

## Instructions for Builder
1.  Read `directives/product_spec.md` for context.
2.  Use Python (PyAudio, OpenAI SDK).
3.  Keep it simple. CLI only.
