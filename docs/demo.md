# Demo: Example Skills

This repo includes two example skills under `.agents/skills/`. Run both before starting your task.

## 1. explain-paper

A simple single-agent skill. Read [SKILL.md](../.agents/skills/explain-paper/SKILL.md) to see how it works, then run:

```
Explain papers/brown2020_gpt3_few_shot.pdf
```

## 2. literature-review

A multi-agent loop using the Ralph Wiggum pattern. Read [SKILL.md](../.agents/skills/literature-review/SKILL.md) carefully -- you will use this pattern in your task.

```
Literature-review papers in the papers/ folder.
```

Notice how it uses `progress.txt` and `learning.txt` to pass state between agents. Each sub-agent reads these files, does one task, updates them, and stops.
