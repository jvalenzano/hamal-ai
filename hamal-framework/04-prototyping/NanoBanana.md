# Hamal UI - Nano Banana Pro Prompts

**Purpose:** Prompts and design specifications for generating high-fidelity UI mockups  
**Tool:** Google Nano Banana Pro  
**Style:** Modern agentic UI, dark mode, glassmorphism accents

---

## 🎨 Design System Reference

> **Include this context at the start of each prompt for consistency.**

### Style Keywords
```
Modern SaaS dashboard, dark mode, glassmorphism, subtle gradients, 
professional tech aesthetic, clean typography, rounded corners (12px), 
soft shadows, blue accent color, minimal but premium feel
```

### Color Palette

| Token | Hex | Usage |
|-------|-----|-------|
| `--bg-primary` | `#0F172A` | Main background (slate-900) |
| `--bg-secondary` | `#1E293B` | Cards, panels (slate-800) |
| `--bg-tertiary` | `#334155` | Hover states (slate-700) |
| `--accent-blue` | `#3B82F6` | Primary actions, links |
| `--accent-blue-glow` | `#60A5FA` | Hover/active states |
| `--success` | `#10B981` | GO, complete, success |
| `--warning` | `#F59E0B` | Conditional, in-progress |
| `--danger` | `#EF4444` | NO-GO, errors |
| `--text-primary` | `#F8FAFC` | Headings, body text |
| `--text-secondary` | `#94A3B8` | Labels, muted text |
| `--border` | `#334155` | Card borders, dividers |

### Typography
- **Font Family:** Inter (headings), JetBrains Mono (code/data)
- **H1:** 32px, Semibold, tracking -0.02em
- **H2:** 24px, Semibold
- **Body:** 16px, Regular
- **Small:** 14px, Medium
- **Mono:** 14px, JetBrains Mono

### Visual Effects
- **Cards:** `rgba(30, 41, 59, 0.8)` with `backdrop-blur(12px)`, 1px border `#334155`
- **Shadows:** `0 4px 24px rgba(0, 0, 0, 0.3)`
- **Border radius:** 12px (cards), 8px (buttons), 6px (inputs)
- **Glassmorphism:** Apply to floating panels, modals, progress cards

---

## 📱 Screen Prompts

### Prompt 1: Project Input Screen

```
Create a high-fidelity UI mockup for a web application input screen.

CONTEXT: This is "Hamal" - an AI-powered idea validation tool that runs concepts 
through 5 rigorous phases before building. The user submits their idea here.

LAYOUT:
- Desktop viewport: 1440x900px
- Dark background (#0F172A)
- Centered content area (max-width 720px)
- Top navigation bar with logo "HAMAL" on left (blue diamond icon), 
  "History" dropdown on right

MAIN CONTENT:
1. Headline: "Validate Your Idea Before Building" (32px, white, centered)
2. Subhead: "Run your concept through 5 rigorous phases of validation 
   before writing a single line of code." (16px, gray, centered)

3. Input Card (glassmorphism panel, centered):
   - Project Name field (text input, placeholder: "e.g., Echo - Second Brain")
   - Large textarea (6 rows): "Describe your idea, paste meeting notes, 
     or upload a document..."
   - Upload button: "📎 Upload document (PDF, Word, TXT)" with ghost button style
   - Divider line
   - Two dropdown selects side by side:
     - "Category" (Consumer App, B2B SaaS, Government, Hardware)
     - "Timeline" (No rush, 3-6 months, <3 months, ASAP)

4. Primary CTA Button: "▶ Run 5-Phase Validation" (blue gradient, full width)
   - Below button: "⏱️ Estimated: 15-20 minutes" (small gray text)

5. Phase Preview (bottom of card):
   Five small horizontal pills/badges showing phases:
   "Research → Validate → Architect → Prototype → Decide"
   Each pill has a subtle icon and muted styling

STYLE:
- Dark mode, glassmorphism card with subtle blue glow
- Blue accent color (#3B82F6) for primary button and focus states
- Rounded corners (12px), soft shadows
- Premium, modern SaaS aesthetic like Linear or Raycast
- No device frames, just the UI itself

OUTPUT: Clean UI mockup, no annotations, production-ready visual
```

---

### Prompt 2: Execution Progress Screen

```
Create a high-fidelity UI mockup for a real-time progress dashboard.

CONTEXT: This is "Hamal" - an AI validation tool. The user has submitted their 
idea and is watching 5 AI phases execute in real-time. Takes ~15-20 minutes total.

LAYOUT:
- Desktop viewport: 1440x900px
- Dark background (#0F172A)
- Two-column layout: Left sidebar (320px) + Main content area
- Top bar: "HAMAL" logo, project name, "Copy Link" and "← Back" buttons

HEADER SECTION:
- Project name: "Echo - Second Brain Concept" (24px, white)
- Progress bar: blue animated gradient, 45% complete
- Time remaining: "⏱️ ~8 minutes remaining" (gray text)

LEFT COLUMN - PHASE STATUS:
Vertical list of 5 phases with status indicators:

1. ✅ Phase 1: Research (4m)
   - Nested bullets: "6 competitors found", "3 market trends"
   - Green checkmark, completed styling

2. 🔄 Phase 2: Validation (now)
   - Animated spinner icon
   - Nested: "Problem validated ✓", "Scoring assumptions..."
   - Yellow/amber active styling with subtle pulse/glow

3. ⏳ Phase 3: Architecture
   - Grayed out, queued state
   
4. ⏳ Phase 4: Prototyping (queued)

5. ⏳ Phase 5: Decision (queued)

Bottom note: "ⓘ You can close this tab. Your results will be saved."

RIGHT COLUMN - LIVE OUTPUT:
Glassmorphism panel showing real-time agent output:
- Header: "Phase 2: Validation" with blue accent
- Streaming text content showing:
  - "✓ User problem validated: 'Knowledge capture friction'"
  - "✓ Primary assumption identified..."
  - Progress bar for current sub-task: "Scoring assumptions... 50%"
- Earlier Activity section with timestamped log entries

STYLE:
- Dark mode with blue and green accent colors
- Active phase has subtle amber glow effect
- Completed phases have green checkmarks
- Queued phases are muted/grayed
- Terminal/log aesthetic for the live output area
- Smooth, polished UI like GitHub Actions or Vercel deployment view

OUTPUT: Clean UI mockup, no annotations, production-ready visual
```

---

### Prompt 3: Results Dashboard - Summary Tab

```
Create a high-fidelity UI mockup for a validation results dashboard.

CONTEXT: This is "Hamal" - an AI validation tool. All 5 phases are complete. 
The user sees their recommendation and key findings.

LAYOUT:
- Desktop viewport: 1440x900px
- Dark background (#0F172A)
- Full-width layout with centered content (max-width 1200px)
- Tab navigation below header

HEADER:
- "HAMAL" logo
- Project name: "Echo - Second Brain Concept"
- Timestamp: "Completed 4:32pm"
- "Export ▼" dropdown and "Share" button on right

TAB BAR:
Four tabs: Summary (active/selected), Reports, Similar, Export
Active tab has blue underline and brighter text

MAIN CONTENT:

1. RECOMMENDATION CARD (hero section, centered):
   Large glassmorphism card with amber/yellow accent border
   - Badge: "CONDITIONAL GO" (amber background, dark text)
   - Three metric boxes inline:
     - Feasibility Score: 35/50 (progress bar)
     - Confidence Level: 7.2/10 (progress bar)
     - Est. Cost: "$45K (8 weeks)"
   - Conditions list with ⚠️ icon:
     - "Software-first approach (no hardware for MVP)"
     - "Target Obsidian power users"
     - "Conduct 5 Mom Test interviews during build"

2. KEY FINDINGS GRID (2x2 cards):
   Four cards showing phase summaries:
   
   📊 Research card:
   - "6 direct competitors found"
   - "Market size: $4.3B (2025)"
   - "Key gap: Local-first privacy"
   - "View Full Report →" link
   
   ✓ Validation card:
   - "Problem validated: Yes"
   - "Riskiest assumption: Trust in ambient capture"
   - "Risk score: Medium (6/10)"
   
   🏗️ Architecture card:
   - "Recommended: PWA + Local LLM"
   - "Complexity: Medium"
   
   📝 Prototyping card:
   - "MVP scope: 4 core features"
   - "Timeline: 8 weeks"

3. DECISION SECTION (bottom):
   - "Record Your Decision" label
   - Three toggle buttons: GO (green), CONDITIONAL GO (amber, selected), NO-GO (red)
   - Notes textarea: "Moving forward with PWA approach..."
   - "Save Decision & Close" button

STYLE:
- Dark mode, premium dashboard aesthetic
- Amber/yellow accent for CONDITIONAL GO recommendation
- Cards have subtle glassmorphism effect
- Progress bars use semantic colors
- Clean data visualization, no chart junk
- Similar to Linear, Notion, or modern analytics dashboards

OUTPUT: Clean UI mockup, no annotations, production-ready visual
```

---

### Prompt 4: Results Dashboard - Reports Tab

```
Create a high-fidelity UI mockup for a markdown report viewer.

CONTEXT: This is "Hamal" validation results. User is viewing the full 
markdown reports generated by each phase.

LAYOUT:
- Desktop viewport: 1440x900px
- Dark background (#0F172A)
- Same header as Summary screen
- Tab bar with "Reports" tab selected

MAIN CONTENT:
Accordion/collapsible sections for each phase report:

1. "▼ Phase 1: Research" (expanded)
   - [Copy] button on right
   - Rendered markdown content in a code-editor style panel:
     - "# Echo Research Report"
     - "## Competitive Landscape"
     - "### Direct Competitors"
     - Numbered list with competitor details (Limitless, Rewind.ai, Otter.ai)
     - Proper markdown formatting with headers, bold text, bullet points
   - Monospace font (JetBrains Mono)
   - Syntax highlighting for markdown
   - Dark code block background (#1E293B)

2. "▶ Phase 2: Validation" (collapsed)
   - Just shows header with [Copy] button

3. "▶ Phase 3: Architecture" (collapsed)

4. "▶ Phase 4: Prototyping" (collapsed)

5. "▶ Phase 5: Decision" (collapsed)

STYLE:
- Dark mode with rendered markdown styling
- Expanded section has code-editor aesthetic (like VS Code dark theme)
- Collapsible chevrons for accordion
- Copy buttons have subtle hover states
- Clean documentation viewer feel like GitBook or Notion in dark mode
- Proper spacing between sections

OUTPUT: Clean UI mockup, no annotations, production-ready visual
```

---

### Prompt 5: Results Dashboard - Similar/Competitors Tab

```
Create a high-fidelity UI mockup for a competitor analysis grid.

CONTEXT: This is "Hamal" validation results. User is viewing competitors 
and similar projects discovered during research.

LAYOUT:
- Desktop viewport: 1440x900px
- Dark background (#0F172A)
- Tab bar with "Similar" tab selected

MAIN CONTENT:
Grid of competitor/similar project cards (3 columns, 2 rows):

ROW 1:
1. Limitless card:
   - 🎧 icon
   - Name: "Limitless"
   - Description: "AI wearable pendant, $99 one-time"
   - Threat level badge: "HIGH" (red)
   - "Key weakness: Privacy (cloud processing)"
   - [Visit Site ↗] button

2. Rewind.ai card:
   - 🔄 icon
   - Name: "Rewind.ai"
   - Description: "Screen + audio capture for Mac, $19/mo"
   - Threat level: "MEDIUM" (amber)
   - "Key weakness: Desktop only"

3. Otter.ai card:
   - 🎤 icon
   - Name: "Otter.ai"
   - Description: "Meeting transcription, $16.99/mo"
   - Threat level: "LOW" (green)
   - "Key weakness: Meetings only"

ROW 2:
4. Mem.ai card
5. Notion AI card
6. Obsidian card (with "PARTNER" badge in blue instead of threat level)

CARD STYLE:
- Dark glassmorphism cards (#1E293B with blur)
- Icon in top left
- Threat level as colored badge
- Divider line between description and weakness
- Subtle hover effect with border glow
- Consistent spacing and alignment

OVERALL STYLE:
- Grid layout with even spacing
- Cards have the same height
- Threat badges use semantic colors (red/amber/green/blue)
- Clean, scannable competitor analysis view
- Similar to a VC research dashboard or Crunchbase

OUTPUT: Clean UI mockup, no annotations, production-ready visual
```

---

### Prompt 6: Export Tab

```
Create a high-fidelity UI mockup for an export/download interface.

CONTEXT: This is "Hamal" validation results. User wants to download 
their validation artifacts.

LAYOUT:
- Desktop viewport: 1440x900px
- Dark background (#0F172A)
- Tab bar with "Export" tab selected

MAIN CONTENT:

1. PRIMARY EXPORT CARD:
   Large card with package icon
   - "📦 All Reports (ZIP)"
   - "Download all 5 phase reports as markdown files"
   - Contents preview: "research.md, validation.md, architecture.md..."
   - Large blue [Download ZIP] button

2. PDF EXPORT CARD:
   - "📄 Executive Summary (PDF)"
   - "One-page overview with decision, key findings, and next steps"
   - [Generate PDF] button (secondary style)

3. INDIVIDUAL FILES SECTION:
   Card with list of files:
   - Checkbox + filename + [Download] + [Copy to Clipboard] for each:
     - ☐ research.md
     - ☐ validation.md
     - ☐ architecture.md
     - ☐ prototyping.md
     - ☐ decision.md

4. ACTIONS SECTION (bottom):
   Two side-by-side cards:
   
   Left card - "🔄 Re-run Phase":
   - Dropdown: "Select phase: [Phase 1 ▼]"
   - [Re-run] button
   - For iterating on specific phases
   
   Right card - "📂 Fork to Project Folder":
   - "Create /ventures/echo/ with all artifacts"
   - Path preview field
   - [Create Folder] button

STYLE:
- Dark mode, clean export interface
- Primary download button is prominent blue
- Secondary actions use ghost/outline button styles
- Checkboxes have custom styling matching dark theme
- Cards have consistent spacing
- Utility-focused, no unnecessary decoration

OUTPUT: Clean UI mockup, no annotations, production-ready visual
```

---

### Prompt 7: Historical View (Phase 2 Feature)

```
Create a high-fidelity UI mockup for a project history list view.

CONTEXT: This is "Hamal" home screen showing past validations. 
User can see all their previous idea validations.

LAYOUT:
- Desktop viewport: 1440x900px
- Dark background (#0F172A)
- Top bar: "HAMAL" logo, [+ New Validation] button on right

MAIN CONTENT:

1. HEADER:
   - "Your Validations" (28px heading)
   - Search bar with placeholder "🔍 Search..."
   - Filter dropdowns: [All ▼] [Date ▼]

2. PROJECT LIST (3 stacked cards):

   Card 1 (most recent):
   - Icon: 📊
   - Title: "Echo - Second Brain" 
   - Date: "Jan 10, 2026"
   - Badge: "CONDITIONAL GO" (amber)
   - Tags: "Consumer App" | "8 weeks / $45K"
   - Key insight: "Local-first privacy is the differentiator"
   - Action buttons: [View Results] [Export] [Archive]

   Card 2:
   - "TrailWatch - Forest Monitoring"
   - "Jan 5, 2026"
   - Badge: "GO" (green)
   - "Government" | "12 weeks / $80K"
   - Insight: "USDA has active RFP, timing is critical"

   Card 3:
   - "FAA Modernization"
   - "Dec 20, 2025"
   - Badge: "NO-GO" (red)
   - "Government" | "Too complex"
   - Insight: "Compliance burden exceeds small team capacity"

CARD STYLE:
- Horizontal card layout (not grid)
- Decision badge prominent on right side
- Metadata in muted text
- Key insight highlighted
- Hover state shows full actions
- Subtle dividers between cards

OVERALL STYLE:
- Clean list view like Linear's issue list or Notion database
- Scannable, information-dense but not cluttered
- Decision badges use semantic colors
- Search/filter area is functional but minimal
- Empty state not shown (we have data)

OUTPUT: Clean UI mockup, no annotations, production-ready visual
```

---

## 🧩 Component Prompts

### Prompt: Decision Badge Component

```
Create a set of status badge UI components for dark mode.

Create 4 badge variants, each 120px wide, pill-shaped, displayed horizontally:

1. "GO" badge:
   - Background: Green (#10B981)
   - White text, bold
   - Subtle shadow

2. "CONDITIONAL GO" badge:
   - Background: Amber (#F59E0B)
   - Dark text (#1E293B), bold
   - Slightly wider to fit text

3. "NO-GO" badge:
   - Background: Red (#EF4444)
   - White text, bold

4. "IN PROGRESS" badge:
   - Background: Blue (#3B82F6)
   - White text
   - Animated pulse effect suggested

STYLE:
- Pill shape (full rounded corners)
- Consistent height (28-32px)
- Bold text, centered
- No device frames, just the components on dark background (#0F172A)

OUTPUT: Component sheet showing all 4 badges
```

---

### Prompt: Phase Status Icons

```
Create a set of phase status indicator components for dark mode.

Show 4 status states, each as a small icon + label combination:

1. COMPLETED:
   - Green circle with white checkmark ✓
   - "Phase 1: Research" label
   - "(4 min)" duration in muted text
   - Green tint overall

2. IN PROGRESS:
   - Animated spinner/loading icon (amber/yellow)
   - "Phase 2: Validation" label
   - "now" in amber text
   - Subtle amber glow effect

3. QUEUED:
   - Gray hourglass or clock icon ⏳
   - "Phase 3: Architecture" label
   - Muted/grayed out styling

4. ERROR (edge case):
   - Red X icon
   - "Phase Failed" label
   - Red accent

STYLE:
- Icons are 20-24px
- Monospace or clean sans-serif labels
- Dark background (#0F172A)
- Suitable for use in a vertical list

OUTPUT: Component sheet showing all 4 states stacked vertically
```

---

### Prompt: Progress Bar Component

```
Create a progress bar component for dark mode dashboard.

Show a horizontal progress bar at different states:

1. 0% - Empty state (just the track)
2. 45% - Mid-progress with animated blue gradient
3. 100% - Complete with green fill

SPECIFICATIONS:
- Width: 400px
- Height: 8px
- Track color: #334155 (slate-700)
- Fill gradient: #3B82F6 → #60A5FA (blue gradient)
- Complete state: #10B981 (green)
- Rounded ends (full radius)
- Subtle inner shadow on track
- Animated shimmer effect on active progress

Also show a secondary circular progress variant:
- 60px diameter
- Same color scheme
- Percentage text in center

STYLE:
- Dark background (#0F172A)
- Clean, modern progress indicators
- No labels, just the bars themselves

OUTPUT: Component sheet with all progress bar variants
```

---

## 🖼️ Additional Assets to Generate

### Empty State Illustration
```
Create a minimal illustration for an empty state in a dark mode dashboard.

SCENE:
- Abstract geometric shapes suggesting "ideas" or "lightbulbs"
- Floating cubes, spheres, or document icons
- Blue and purple gradient accents
- No characters or people
- Suitable as a 300x200px spot illustration

TEXT SUGGESTION (do not render):
"No validations yet. Start by describing your idea."

STYLE:
- Minimal, geometric, abstract
- Dark theme compatible (light illustration on dark)
- Modern SaaS aesthetic
- Not too detailed - works at small size

OUTPUT: Spot illustration without text
```

### Logo Concept
```
Create a minimal logo mark for "Hamal" - an AI-powered idea validation tool.

CONCEPT:
- Abstract geometric shape suggesting "filtering" or "validation"
- Could incorporate: diamond, prism, funnel, or 5-sided shape (for 5 phases)
- Blue as primary color (#3B82F6)
- Works on dark backgrounds

VARIATIONS:
1. Icon only (square format for favicon)
2. Icon + "HAMAL" wordmark (horizontal lockup)

STYLE:
- Minimal, geometric, tech-forward
- Single color or simple gradient
- Clean lines, no gradients in icon mark
- Would work as a 32x32 favicon

OUTPUT: Logo concepts on dark background
```

---

## 📐 Layout Templates

### Prompt: Dashboard Grid System

```
Create a wireframe grid overlay for a dark mode dashboard.

SPECIFICATIONS:
- Viewport: 1440x900px
- 12-column grid
- 24px gutters
- 80px margins on left/right
- 64px top navigation area
- 48px tab bar area

SHOW:
- Column guides (light blue/cyan lines)
- Gutter spacing
- Safe areas marked
- Baseline grid (8px vertical rhythm)

STYLE:
- Dark background (#0F172A)
- Grid lines in cyan/light blue at 20% opacity
- Annotations showing measurements
- No actual UI content, just the grid system

OUTPUT: Annotated grid template
```

---

## 🎬 Interaction State Prompts

### Button States
```
Create a button component sheet showing interactive states.

PRIMARY BUTTON (blue):
- Default: Blue background (#3B82F6), white text
- Hover: Lighter blue (#60A5FA), subtle lift shadow
- Active/Pressed: Darker blue, pressed effect
- Disabled: Muted gray, 50% opacity

SECONDARY BUTTON (ghost/outline):
- Default: Transparent with border
- Hover: Subtle fill
- Active: Darker fill
- Disabled: Muted

DANGER BUTTON (red):
- Same states as primary but red

SPECIFICATIONS:
- Height: 44px
- Padding: 16px 24px
- Border radius: 8px
- Font: 16px, Medium weight

STYLE:
- Dark background (#0F172A)
- Show all states in a grid layout

OUTPUT: Button component sheet
```

---

## Usage Notes for UX Designer

1. **Run each prompt separately** - Don't combine prompts
2. **Iterate** - If output isn't right, refine specific elements
3. **Consistency** - Reference the Design System section in each prompt
4. **No device frames** - We want raw UI, not laptop/phone mockups
5. **Dark mode first** - All designs should be dark theme

### Prompt Refinement Tips
- Add "in the style of [Linear/Raycast/Vercel]" for specific aesthetics
- Use "no text labels" if you only want the visual layout
- Add "with realistic content" if placeholder text looks off
- Use "annotated with measurements" for dev handoff versions

---

**File Location:** `hamal-framework/04-prototyping/NanoBanana.md`  
**Companion File:** `hamal-framework/04-prototyping/hamal-ui-wireframes.md`
