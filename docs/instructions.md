# Sprint M03: Build a Personalized Assistant

## Goal

Build an AI assistant that solves a real problem for *you* and improves through your feedback.

---

## Setup (do this once)

1. **Fork** this repo on GitHub (top-right → Fork).
2. Open your fork in **GitHub Codespaces**.
3. Get a free API key from [Ollama Cloud](./ollama.md) or [OpenRouter](./openrouter.md).
4. Open OpenCode: `Ctrl+Shift+P` → `OpenCode: Open opencode`
5. Connect your key: type `/connect` in the OpenCode terminal.
6. Install dependencies: type `/setup`

---

## What to Build

Pick any assistant that is genuinely useful to you. Examples:

| Assistant | What it does |
|---|---|
| Literature Assistant | Searches and summarizes research papers |
| News Briefing | Delivers daily news in your preferred tone and focus |
| Anything useful | Your call — just make it solve a real problem |

**Your assistant must implement all three context engineering primitives:**

| Primitive | What it means | Example |
|---|---|---|
| **Write** | Persist state to files | Save feedback to `preferences.md` |
| **Select** | Pull in relevant context selectively | Search papers before answering |
| **Isolate** | Delegate subtasks to sub-agents via the Task tool | One agent fetches, another synthesizes |

---

## Steps

### Step 1 — Vibe (prototype)
Build something rough with no planning. Goal: understand what is hard. Mess is expected.

### Step 2 — Plan
Open a fresh session (`/new`) and paste this prompt (fill in `[ASSISTANT]` and `[ASSISTANT-NAME]`):

```
I want to build a personalized AI assistant called [ASSISTANT] under .agents/skills/[ASSISTANT-NAME].
Interview me RELENTLESSLY until nothing is ambiguous. Ask one question at a time.
Cover: what it does, how it learns preferences, how users give feedback, inputs, outputs, edge cases, tools, output format.
Then write PRD.md with each task as:

## Task <N>: <name>
- Implemented: false
- Test Passed: false
- Goal / Inputs / Outputs / Specifications / Test Case / Evaluation Criteria
```

Commit `PRD.md` when done.

### Step 3 — Implement
Start a new session and implement your skill according to `PRD.md`. Commit your `.agents/skills/` folder.

### Step 4 — Teach it your preferences
Run the assistant on at least **3 different inputs**. After each run, give feedback:
```
I didn't like [X]. Next time, [Y].
Tell me what you've learned about my preferences.
```
Verify that feedback is saved to `preferences.md` and applied on the next run.

### Step 5 — Test and iterate
Run `/test-skill` or write your own test. Fix until you are satisfied.

---

## Tips

- **Commit often.** After each task, commit with a clear message. This creates a second-brain for the agent and lets you roll back.
- **Keep `SKILL.md` short.** Under ~150 lines is ideal. If it grows too long, try: `condense the skill by sacrificing grammar while keeping every point intact.`
- **Stop your Codespace when done** at [github.com/codespaces](https://github.com/codespaces) to preserve your free quota.
- **Push your work** with `git push` so it is safe even if the Codespace is deleted.
