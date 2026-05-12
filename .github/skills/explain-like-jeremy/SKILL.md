---
name: explain-like-jeremy
description: >
  Produces a Jeremy Howard-style (fast.ai) top-down explainer of any codebase.
  Use when you want to understand a project from the big picture down to the
  code, see a working demo before theory, or learn by analogy. Triggered by
  phrases like "explain this repo", "how does this work", "give me a tour",
  "walk me through", "help me understand", "Jeremy Howard style".
argument-hint: 'Optional: a specific subsystem or concept to focus on (e.g. "authentication", "data pipeline", "frontend")'
---

# Explain Like Jeremy (fast.ai style)

## Teaching Philosophy

Follow this order strictly — don't break it for any reason:

1. **Demo first** — show the end result before any theory.
2. **Top-down** — start with the whole system, drill into one part the learner cares about.
3. **Concrete before abstract** — code or output first, then the mental model.
4. **One analogy per concept** — pick the most apt one and stick with it.
5. **"Now you can ignore X"** — name the things being deliberately simplified; honesty builds trust.
6. **Spiral back** — revisit early simplifications once the learner has enough context.

---

## Step 1: Demo (show, don't tell)

Open with what the user would *experience* if the project were running right now.
Describe what they would see, interact with, or observe — output first, not architecture.

> Example pattern: "If you ran this right now, you'd see [observable behaviour].
> Under the hood, [component A] is doing [thing], while [component B] handles [thing].
> You are watching [N] separate pieces working together."

If a narrower focus was requested (e.g. "authentication"), demo just that slice.
Explore the codebase first (read `README.md`, entry-point files, and any existing
architecture docs) to make the demo description accurate.

---

## Step 2: The whole thing in one sentence

State the system in ≤30 words. Write it as a declarative fact:

> "[Project name] is a [what it does] where [key components] [how they interact],
> with [central piece] in the middle [what it does]."

Derive this from the README and top-level structure — don't invent.

---

## Step 3: Top-down map (one diagram pass)

Explore the repo structure, then present the major layers in order from user-facing
to infrastructure. For each layer, name the *file the learner should open first*:

| What it does | File to open first |
|---|---|
| [Layer N — user-facing, e.g. UI / CLI] | `path/to/entry.ext` |
| [Layer N-1 — e.g. API / gateway] | `path/to/entry.ext` |
| [Layer N-2 — e.g. core business logic] | `path/to/entry.ext` |
| [Layer N-3 — e.g. data / infra] | `path/to/entry.ext` |

If the repo has an architecture diagram or Mermaid chart, surface it here.
Otherwise offer to generate one.

---

## Step 4: Walk through one complete interaction

Pick the most representative user action (a request, a command, a job run) and
trace it end-to-end. Keep it to **6 steps, no more**. Number them. Be concrete:
name the actual files and functions involved.

Close with one memorable analogy that covers the whole flow, e.g.:
*"[Component A] is the [relatable role]. [Component B] is [relatable role].
[Component C] is [relatable role]."*

---

## Step 5: Drill into the requested subsystem

If the user specified a subsystem in their argument, go deeper now.
Otherwise ask: *"Which piece interests you most — [list the top 3–4 components
you found in Step 3]?"*

For the chosen subsystem, follow this pattern:

1. **Entry point** — the single file to open first.
2. **What it does** — one sentence.
3. **Key internal structure** — the 2–3 most important functions/classes and
   what they do. Read the actual code before describing it.
4. **Analogy** — one concrete analogy for this subsystem's role.
5. **Simplification to name** — what you are glossing over and why it's safe to.

If variants or alternative implementations exist (e.g. basic vs. advanced version),
frame them as *progressive chapters*, not alternatives to pick from.

---

## Step 6: Name the deliberate simplifications

Always close with what was glossed over and *why it's safe to ignore for now*.
Aim for 3–5 items. Draw these from what you actually found in the codebase —
don't invent complexity. Format:

- **[Thing]** — [what it does]; safe to ignore until [specific trigger].
- **[Thing]** — [what it does]; ignore unless [specific use case].

---

## Step 7: What to try next

Give the learner **one** concrete next action — a command to run, a file to open,
or a small change to make. Make it specific and immediately actionable:

```
# Example (adapt to the actual project):
[command to run the project or a demo]
```

Then give one sentence on the single best file to read next and why:
*"Once that's running, the best next thing to read is `path/to/file` —
it's [what it does] in ~[N] lines."*

---

## Codebase exploration guide

Before answering, gather context in this order:

1. Read `README.md` for project purpose and quick-start.
2. List the top-level directory to identify layers.
3. Read entry-point files (e.g. `main.*`, `app.*`, `index.*`, `agent.py`).
4. Check for existing architecture docs (`docs/`, `ARCHITECTURE.md`, diagrams).
5. Read one representative "happy path" file per major layer.

Do not fabricate file paths or component names. Only reference what you find.

---

## Quality checks before finishing

- [ ] Did you show the output/result before explaining the code?
- [ ] Is every technical term accompanied by an analogy on first use?
- [ ] Did you explicitly name at least two things being simplified?
- [ ] Is the explanation scoped to what the learner asked — no more?
- [ ] Are all file paths verified against the actual workspace?
- [ ] Is there exactly one "what to try next" action at the end?
