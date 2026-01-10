---
description: Conducts market and competitive research for a new idea using Search and Reasoning agents.
---
# Workflow: Research Idea

This workflow is the first step in the Hamal Framework. It gathers data to determine if an idea has market potential.

## Step 1: Define the Problem Space
**Action:** User provides a 1-sentence "Shower Thought" idea.
**Agent Task:** `search_web` to understand the domain, jargon, and current trends.

## Step 2: Competitive Landscape
**Agent Task:** `search_web` for direct and indirect competitors.
**Output:** List of 3-5 major players, their value props, and pricing.

## Step 3: "Why Now?" Analysis
**Agent Task:** Analyze why this problem hasn't been solved yet (or badly solved). Look for technological, regulatory, or cultural shifts.

## Step 4: Deliverable
**Agent Task:** Create `hamal-framework/01-research/[idea-name]-research.md` containing:
1.  Problem Statement
2.  Competitive Chart
3.  Market Headwinds/Tailwinds
4.  Initial Feasibility Rating (Low/Med/High)
