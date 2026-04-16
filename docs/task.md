# Your Task: Build a Personalized Assistant

Design and build an AI assistant that makes *your* life or work easier. The assistant must learn your preferences over time and improve through your feedback.

## What to Build

Pick an assistant that solves a real problem for you. Here are some example ideas. You can build assistant for other use cases too. 

| Idea | What it does |
|---|---|
| **Literature Assistant** | Given a research question, searches and summarizes relevant papers using the [OpenAlex CLI](https://github.com/alejandroschuler/openalex) |
| **Personalized News Briefing** | Fetches today's news and delivers a briefing in the tone, style, and focus areas you specify |
| **Anything else** | It just has to be useful to *you* |

The assistant should improve the more you use it: when you give feedback ("be more concise", "focus on methods, not results"), the assistant remembers and applies it next time.

## Requirements

Your `SKILL.md` must implement all three context engineering primitives:

### 1. Write — persist state
The assistant must save data to files. Examples:
- A preferences file (`preferences.md`) that stores your feedback and style instructions
- A history file that logs past queries and responses
- A memory file that accumulates domain knowledge across sessions

### 2. Select — retrieve relevant context
The assistant must selectively pull in context rather than dumping everything into every prompt. Examples:
- Retrieve relevant past notes or papers before answering
- Query an external API or dataset (e.g., OpenAlex for papers, a news API for headlines)
- Search the web for current information

### 3. Isolate — use sub-agents
The assistant must delegate subtasks to isolated sub-agents via the Task tool. Examples:
- One sub-agent fetches/searches; another synthesizes
- One sub-agent reads your preferences and plans; another executes
- Parallel sub-agents handle independent pieces of a request

---

## Steps

### Step 1: Vibe

Build a rough prototype with no planning. Goal: get a feel for what is hard. The output will be messy. That is intentional.

> [!TIP]
> Instruct agents to make an atomic commit with a clear message after each task. The git log becomes a second-brain of the agent, recording what was done, when, and why. It also lets you roll back easily if something goes wrong.

### Step 2: Plan

Create a clear, unambiguous specification. Every ambiguity becomes a silent decision the agent makes during implementation—usually wrong.

Discard the prototype. Open a fresh session (`/new`).

Paste this prompt (replace `[ASSISTANT]` and `[ASSISTANT-NAME]`):

```
I want to build a personalized AI assistant called [ASSISTANT] under .agents/skills/[ASSISTANT-NAME].
Interview me RELENTLESSLY until nothing is ambiguous.
Ask one question at a time. Cover: what the assistant does, how it learns my preferences,
how users give feedback, inputs, outputs, edge cases, tools, and output format.
Then write PRD.md with overview and each task as a subsection:

## Task <N>: <name>
- Implemented: true/false  (set to true once SKILL.md/code for this task is written)
- Test Passed: true/false  (set to true once test-skill confirms output meets criteria)
- Goal:
- Inputs:
- Outputs:
- Specification 1:
- Specification 2:
- ... (as many specs as needed)
- Test Case (optional):
- Evaluation Criteria (optional):
```

**Output:** `PRD.md`

git commit `PRD.md`.

---

# Step 3: Implement

Clear the memory and start implementing the skill according to the plan and PRD.md. git commit your SKILL folder. 

> [!TIP]
> Shorter instructions are better—for the agent and for you. If `SKILL.md` exceeds ~150 lines, create templates or tools to offload parts of the process.
>
> If your instruction is longer than that, try `condense the skills by sacrificing grammar while keeping every point intact. No markdown decolation unless necessary.`. Agents follow grammar rules too strictly, leading to unnecessary verbosity. Explicitly permitting grammar sacrifices encourages tighter, more task-oriented output.


# Step 4: Test and Iterate

Let's test the skill. You can reopen opencode and give a test prompt, or you can simply create a new "test-skill" skill that instructs the agent to spaw a sub-agent to run the skill for a predefined prompt. I created an example, non-tested test-skill in `.agents/skills/test-skill


### Step 3: Teach It Your Preferences

Run your assistant on at least three different inputs. After each run, give it feedback, e.g., 

```
I didn't like [X]. Next time, [Y].
Tell me what you've learned about my preferences.
```

Verify that the assistant:
- Saves your feedback to `preferences.md` (or equivalent)
- Applies it on the next run without you repeating yourself

---

## Step 4: Test and Iterate 


Run your skill on the tests you designed. Fix the skill until you are satisfied.

