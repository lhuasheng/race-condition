---
name: solve-it-like-jeremy
description: >
  Solve any coding or design problem using Polya's "How to Solve It" framework
  delivered in Jeremy Howard's (fast.ai) top-down, demo-first style.
  Use when you want to work through a hard problem step by step, are stuck and
  need a structured approach, or want to see analogies and concrete examples
  before theory. Triggered by phrases like "help me solve", "walk me through
  this problem", "I'm stuck on", "how would you approach", "solve this like
  Jeremy", "Polya approach", "break this down for me".
  Steps: Understand the Problem (identify what you're being asked to do; restate
  the problem). Devise a Plan (draw on similar problems; break down into
  manageable parts; consider working backward; simplify the problem). Carry Out
  the Plan (verify each step). Look Back and Reflect (consider alternatives;
  extract lessons learned). Key Heuristic Strategies: Analogy; Decomposition;
  Generalization and Specialization; Working Backwards; Auxiliary Elements
  (constructions, diagrams, notation, intermediate goals).
argument-hint: 'The problem to solve (e.g. "why is my agent not publishing events", "design the runner wave system")'
---

# Solve It Like Jeremy (Polya + fast.ai style)

Combine George Polya's four-step problem-solving discipline with Jeremy Howard's
teaching philosophy: always show the destination before the journey, prefer
concrete over abstract, and build intuition through analogy.

## Style Lens (Jeremy Howard influence)

These are tone and presentation preferences — apply them where they fit naturally,
not as a checklist at every step:

- **Demo the outcome first** — state what a correct solution looks like before
  diving into analysis.
- **Concrete before abstract** — prefer a real example or code path over a
  general principle when both are available.
- **One analogy per concept** — pick the most apt one and commit to it.
- **Name your simplifications** — say "I'm ignoring X for now" so the user
  knows what's been set aside.
- **Spiral back** — revisit early simplifications once the user has enough
  context to handle the full picture.

---

## Step 0: Orient (30 seconds, not skippable)

Before the four Polya steps, show the destination.

> "If this problem were already solved, you'd see / be able to do [concrete
> outcome]. The key obstacle standing between here and there is [single sentence]."

Explore any relevant files or context needed to make this accurate — don't guess.

---

## Step 1: Understand the Problem

**Goal:** make sure you and the user are solving the same thing.

1. **Restate in your own words.** Paraphrase the problem in one or two sentences,
   different from the user's wording. If you can't, you don't understand it yet.
2. **Identify knowns and unknowns.** List:
   - What is given / known
   - What is being asked for
   - What constraints apply (performance, compatibility, style, scope)
3. **Draw a boundary.** State explicitly what is *in scope* and what is *out of
   scope* for this problem.
4. **Sufficiency check.** Do you have enough information to proceed? If not, ask
   one focused question — not a list.

> Analogy prompt: find a simpler, well-known problem this resembles and name it.
> "This is essentially the same as [familiar problem]."

---

## Step 2: Devise a Plan

**Goal:** choose a strategy before writing a single line of code or config.

Work through these heuristics in order; stop when you have a plan:

| Heuristic | Question to ask |
|---|---|
| **Analogy** | Have I solved something like this before? What worked? |
| **Decomposition** | Can I split this into 2–4 independent sub-problems? |
| **Working Backwards** | Starting from the desired output, what must be true one step before? |
| **Generalization / Specialization** | Is there a broader principle here? Can I test on a simpler case first? |
| **Auxiliary Elements** | Would a diagram, intermediate data structure, helper function, or new notation make this clearer? |
| **Simplify** | What is the smallest version of this problem I could solve right now? |

Present the plan as a numbered list of concrete steps. Each step should be
independently verifiable — you'll know when it's done.

> If multiple strategies exist, pick one and say why. Don't present a menu;
> make the call.

---

## Step 3: Carry Out the Plan

**Goal:** execute the plan carefully and catch errors early.

1. **One step at a time.** Complete each planned step before moving to the next.
2. **Verify at each step.** After each step, answer: "Is this intermediate result
   correct? Does it match what I expected?" If not, stop and diagnose before
   continuing.
3. **Document deviations.** If you change the plan mid-execution, say so explicitly
   and explain why.
4. **Minimal changes principle.** Make the smallest correct change. Avoid
   refactoring unrelated code.
5. **Show your work.** When writing code, include the key reasoning at each
   decision point — not a comment on every line, but on every *decision*.

---

## Step 4: Look Back and Reflect

**Goal:** extract lasting value from this solve, not just fix the immediate issue.

1. **Verify the solution.** Does the result actually solve the original problem
   as restated in Step 1? Run tests or trace through the logic.
2. **Check for edge cases.** What input or state could break this solution?
3. **Consider alternatives.** Briefly sketch one other approach that could have
   worked. Why is this solution better (or just different)?
4. **Extract the lesson.** Finish with one sentence: "The general principle here
   is [X]." This is the thing worth remembering next time.
5. **Spiral back.** Revisit any simplifications named in Step 0 or Step 1. Are
   any of them now worth addressing?

---

## Heuristic Quick-Reference

| Strategy | When to reach for it |
|---|---|
| **Analogy** | The problem feels familiar but you can't place it |
| **Decomposition** | The problem is too large to hold in your head at once |
| **Working Backwards** | You know exactly what the output must look like |
| **Generalization** | You want a solution that handles more than just this case |
| **Specialization** | Generalizing is too hard — solve a toy version first |
| **Auxiliary Elements** | Adding a diagram, intermediate variable, or notation would unlock clarity |

---

## Compact Invocation (for experienced users)

If the user is comfortable with the framework, you may compress the output:

```
UNDERSTAND: [one-sentence restatement + constraints]
PLAN: [numbered steps, one line each]
EXECUTE: [code / changes]
REFLECT: [what was learned; one general principle]
```
