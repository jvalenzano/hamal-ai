Based on community best practices from Reddit, GitHub, and Antigravity resources, here are comprehensive recommendations for your Global and Workspace rules:[1][2][3][4][5][6][7]

## Global Rules Best Practices
**Location**: `~/.gemini/GEMINI.md` (Mac)

### Structure and Organization

**Keep It Universal** - Only include rules that apply to ALL projects. Framework-specific rules belong in workspace files.[7]

**Start Small, Iterate** - Begin with 5-10 essential rules and expand as patterns emerge. Too many rules upfront can overwhelm the agent.[4][7]

**Include "Don't" Rules** - Explicitly state what NOT to do. Examples from the community:[7]
- No `console.log` in production code
- No `any` types in TypeScript
- No hardcoded credentials
- No inline styles

**Stay Under 6,000 Characters** - GEMINI.md has character limits. Be concise.[7]

### Community-Tested Global Rules Template

From analyzing 100+ Reddit posts:[3]

```markdown
# IDENTITY & COMMUNICATION
* Tone: Technical, concise, and objective
* Skip unnecessary status updates and confirmations
* Present code changes without verbose explanations
* Only explain complex logic when asked

# CODE QUALITY STANDARDS
* Follow language-specific style guides (PEP 8, ESLint, etc.)
* Use descriptive variable names (isLoading, hasError, userData)
* Keep functions under 30 lines when possible
* Add comments only for complex logic and "why" not "what"
* Use early returns to reduce nesting

# ERROR HANDLING
* Always handle errors explicitly with try/catch
* Log errors with context (function name, parameters)
* Never silently swallow errors

# TESTING
* Write tests for business logic
* Use descriptive test names explaining the scenario
* Mock external dependencies

# GIT & COMMITS
* Use conventional commit format (feat:, fix:, docs:)
* Keep commits atomic and focused
* Write clear messages explaining "why" not "what"

# SECURITY & BOUNDARIES
* File-system access limited to workspace only
* No hardcoded credentials or API keys
* Request approval for destructive operations
```

### Key Community Insights

**Use Planning Mode** - Set agent to Planning Mode with review enabled. This prevents code deletion and gives you control over implementation plans.[2][3]

**Review Before Accepting** - Always review implementation plans before accepting. Use Google-Docs-style comments on artifacts to request changes.[3]

**Document Decisions** - Make the agent write decisions in `.md` files after turns. Consolidate every 5 turns to maintain context.[2]

**Meta-Prompt Your Rules** - Use Antigravity itself to generate its own rules. Feed it Claude documentation and best practices, then refine the output.[8]

## Workspace Rules Best Practices

**Location**: `your-workspace/.agent/rules/`

### Organize by Category[5][3]

Create separate files for different concerns:

**`code-style-guide.md`**:
```markdown
* Make sure all code is styled with PEP 8 style guide
* Make sure all code is properly commented
* Use meaningful variable and function names
```

**`code-generation-guide.md`**:[5]
```markdown
* The main method in main.py is the entry point to showcase functionality
* Do not generate code in the main method
* Generate distinct functionality in a new file (e.g. feature_x.py)
* Generate example code in a new method in main.py (e.g. example_feature_x)
* Simply call that method from the main method
```

**`security.md`**:[3]
```markdown
* Never commit secrets or API keys
* Use environment variables for configuration
* Validate all user inputs
* Sanitize data before database queries
```

**`typescript.md`**:[3]
```markdown
* Use strict TypeScript mode
* Prefer interfaces over types for objects
* Use unknown instead of any
* Add JSDoc for public APIs
```

### Artifact-Specific Rules[6]

Antigravity operates in a loop: **Plan → Execute → Verify**. Customize how it uses artifacts:

**task.md rules**:
```markdown
* Always break tasks into granular sub-tasks of no more than 1 hour
* Mark dependencies between tasks explicitly
```

**implementation_plan.md rules**:
```markdown
* Always include a 'Security Implications' section
* List all files to be modified upfront
* Include rollback steps for major changes
```

**walkthrough.md rules**:
```markdown
* Include screenshots or GIFs of UI changes
* Document testing steps performed
```

## Critical Setup Recommendations

**Enable Review-Driven Development**  - Set agent to require review before code execution. Prevents catastrophic mistakes.[3]

**Set Hardware-Appropriate Expectations**  - If you have 16GB RAM (vs. 32GB recommended), add rules about keeping context smaller and using Fast mode more often.[3]

**Use Architecture Documents**  - Create an `architecture.md` in your workspace root. Reference specific lines when adding features to keep the agent focused.[2]

**Create Custom Workflows for Common Tasks** - Save workflows in `~/.gemini/antigravity/global_workflows/` for repeated patterns.

## Priority System

Workspace rules override global rules. Use this hierarchy:[7]
1. Workspace `.agent/rules/` (highest priority - team standards)
2. Global `~/.gemini/GEMINI.md` (personal preferences)

## Quick Win Checklist[3]

- ✅ Create custom rules for your main languages (typescript.md, python.md)
- ✅ Add security.md with non-negotiable security standards  
- ✅ Use artifacts effectively - review plans, not just code
- ✅ Enable Planning Mode with review for complex tasks
- ✅ Set Terminal Policy to "Auto" for standard commands[9]
- ✅ Limit scope to workspace only in secure mode[3]

These practices come from developers who've shipped real projects with Antigravity and learned through trial and error.[1][8][2][3]

[1](https://www.reddit.com/r/google_antigravity/comments/1ptnd90/anyone_got_tips_tricks_hacks_to_actually_enjoy/)
[2](https://www.reddit.com/r/GoogleAntigravityIDE/comments/1pfpe36/how_to_actually_make_antigravity_useful/)
[3](https://www.reddit.com/r/google_antigravity/comments/1pqkb9a/i_analyzed_100_reddit_posts_about_antigravity/)
[4](https://antigravityai.directory/gemini-md-guide)
[5](https://atamel.dev/posts/2025/11-25_customize_antigravity_rules_workflows/)
[6](https://antigravity.codes/blog/user-rules)
[7](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/images/21316841/c92bc1b1-1086-4ae1-a312-7e20282caffc/image.jpg)
[8](https://www.reddit.com/r/google_antigravity/comments/1prpevi/antigravity_and_the_power_of_meta_prompting_rules/)
[9](https://www.codecademy.com/article/how-to-set-up-and-use-google-antigravity)
[10](https://www.reddit.com/r/google_antigravity/comments/1pa9k9x/any_tutorial_guide_available_for_antigravity/)
[11](https://www.reddit.com/r/ClaudeAI/comments/1p1w6am/i_tried_google_antigravity_dont_do_it/)
[12](https://www.reddit.com/r/GoogleAntigravityIDE/comments/1pyhh86/my_honest_experience_with_google_antigravity_bugs/)
[13](https://github.com/study8677/antigravity-workspace-template)
[14](https://dev.to/czmilo/15-essential-google-antigravity-tips-and-tricks-complete-guide-in-2025-3omj)
[15](https://www.reddit.com/r/google/comments/1p10ev8/has_anyone_tried_antigravity_by_google_thoughts/)
[16](https://github.com/lbjlaq/Antigravity-Manager/blob/main/README_EN.md)