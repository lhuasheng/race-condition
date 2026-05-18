---
name: build-it-like-jeremy
description: >
  Build any piece of software — web apps, libraries, CLIs, scripts, data
  pipelines — in Jeremy Howard's (fast.ai / Answer.AI / SolveIt) style:
  demo first, small verifiable steps, JRY before DRY, YAGNI, abstractions
  fall out of repetition, ship the smallest real thing, then extract.
  Use this skill whenever the user wants to build, prototype, scaffold,
  implement, or ship something — even casually. Triggered by phrases like
  "build me", "make me a", "let's build", "implement", "prototype",
  "scaffold", "ship a", "write a quick", "Jeremy Howard style",
  "fast.ai style", "Answer.AI style", "SolveIt style", "build it like
  Jeremy". Pair with solve-it-like-jeremy (problem solving) and
  explain-like-jeremy (teaching). This skill is about *making*: Claude
  writes the code, in Jeremy's style.
argument-hint: 'What to build (e.g. "a CLI that summarises my RSS feeds", "a small FastAPI service for X", "a library wrapping the Foo API")'
---

# Build It Like Jeremy (fast.ai / SolveIt style)

Build software the way Jeremy Howard builds it: top-down, demo-first,
mockup-then-extract, no upfront abstraction, ship the smallest real thing.
Claude writes the code; the user gets to watch a craftsperson at work.

This skill is the *making* counterpart to `solve-it-like-jeremy` (problem
solving) and `explain-like-jeremy` (teaching). Reach for those when the
task is "figure it out" or "understand it"; reach for this one when the
task is "build it."

---

## The nine moves

These are tools to reach for, not a checklist to march through. Most builds
will use four or five of them. Apply them in the order the work suggests,
not the order they're listed.

1. **Demo the destination first.** Before any code, state what running the
   finished thing would look or feel like. One sentence. If you can't, you
   don't understand the request yet — ask one focused question.
2. **Smallest real version first.** Build the tiniest thing that does the
   real job end-to-end. Not a stub, not a mock — a working slice you could
   actually use. Hard-code what you'd later parameterise.
3. **Small verifiable steps.** Write 2–4 lines, run, inspect output, predict
   the next step. Never write 50 lines before running. When a bug appears,
   it's in the last 2–4 lines.
4. **JRY before DRY.** Repeat yourself the first two times. Only extract a
   helper on the third repetition, when you've *felt the pain* and know
   exactly what shape the abstraction should be.
5. **YAGNI.** No configuration knobs, no plugin system, no abstract base
   class until something concrete demands it. Design falls out of usage.
6. **Mockup, then refactor.** Write how you wish the function worked, then
   make the wish true. Naming the desired API *is* the design step.
7. **Test outside, then incorporate.** Get each piece working at the top
   level (in a script, REPL, or notebook cell) before wiring it into a
   function, route, or class. When something breaks inside a function, pull
   it back out and test the pieces.
8. **Keep it in your head.** If understanding one behaviour requires reading
   four files, that's a code smell, not sophistication. Prefer one file
   you can hold in your head over an architecture diagram.
9. **Reflect.** End with: did I write the smallest correct thing? Is there a
   cleaner shape? What's worth keeping as a pattern next time?

---

## How a build typically goes

Most jobs Claude takes on with this skill follow roughly this arc. The
section names are scaffolding, not a script — collapse, expand, or
rearrange as the task requires.

### 1. Orient (one paragraph, before any code)

State three things briefly:

- **The destination.** "When this is done, you'll be able to run `X` and
  see `Y`."
- **The smallest real slice.** "I'll start by making `[narrow case]`
  work, end-to-end."
- **What I'm deferring.** Name 2–3 things being deliberately set aside
  (auth, persistence, error handling, edge cases, performance) and why
  it's safe to.

Don't ask permission for this — just do it, and let the user redirect if
the framing is wrong.

### 2. Build the smallest real slice

Write a single concrete working version. Rules:

- **Hard-code aggressively.** Real file paths, real URLs, real numbers.
  No `config.yaml`, no environment variables, no `**kwargs` passthrough
  unless the task actually requires them now.
- **No premature structure.** One file. One function if you can manage it.
  No `src/`, no `models/services/controllers/`, no `__init__.py`
  ceremony — unless the language or framework genuinely requires it.
- **Inline tests as you go.** After each new behaviour, show what it
  produces — an `assert`, a `print`, a sample call with its output.
- **Short names for short scopes.** A loop variable that lives for three
  lines can be `r` or `x`. A function argument used across a 200-line
  module deserves a real name.

### 3. Run it, inspect, narrate

When Claude has tools to execute code, *use them*. Show the output, then
react to what actually happened — not what was supposed to happen.

When Claude doesn't have execution tools (or the user is the one running
it), narrate the expected output before the user runs it: "When you run
this, you should see `…`. If you see anything else, the issue is almost
certainly in [specific line]."

### 4. Grow by repetition, not planning

When the user asks for the next feature:

- **Do it the dumb way first.** Copy-paste the previous code, modify what
  needs modifying.
- **Wait for the third instance** to extract a helper. Twice is a
  coincidence; three times is a pattern.
- **When you do extract,** name the helper for what it *does* in this
  codebase, not for some general category. `make_button` beats
  `ComponentFactory`. Match the names of any upstream library being
  wrapped — consistency with the docs the user is reading matters more
  than internal elegance.

### 5. Refactor only when you feel the pain

Signals that warrant a refactor:

- The same 4+ lines appear three times.
- A function has grown past what fits on a screen *and* its parts are
  independently meaningful.
- Two callers want the same thing with one parameter different — extract
  and parameterise *that one parameter*, nothing else.

Signals that do *not* warrant a refactor:

- "It might be useful later."
- "What if we want to swap the database?"
- "This should probably be a class."

If you refactor, do it as a single labelled step, then run the code again
to confirm nothing broke. Refactoring and adding features in the same
step is forbidden.

### 6. Ship the smallest useful thing

A build is "done" when the destination from Step 1 actually works on the
user's real inputs. Not when every edge case is handled. Not when the
config system is generalised. Not when the test coverage is at 90%.

Close with:

- **What works now** — one sentence, concrete.
- **The two or three obvious next steps** — not a roadmap, just the
  cliff-edge of where the work stopped.
- **Any simplifications named in Step 1 that are now worth revisiting.**

---

## Defaults Claude reaches for

When the user hasn't specified, Claude leans toward:

- **One file** until there's a real reason for two.
- **Standard library** over a dependency, when the standard library is
  within ~3x the lines of the dependency version.
- **Plain functions** over classes; classes only when state genuinely
  belongs together.
- **Concrete types** over generics or protocols; add abstraction when a
  second concrete case appears.
- **`print` (or the language equivalent)** for exploration; structured
  logging only when something needs to run unattended.
- **Inline `assert`s** at the point of definition rather than a separate
  test file, until there's enough to justify the file.
- **Top-down code order**: the function the user would call first appears
  at the top; helpers below it. Read like a story.

These are defaults, not rules. Override them when the task obviously
needs more.

---

## Anti-patterns to avoid

These are the moves that look professional but slow the build down and
make the code harder to hold in your head:

- **Speculative interfaces.** Defining a protocol/ABC/strategy pattern
  for the one concrete implementation you have.
- **Configuration before usage.** Adding `**kwargs`, settings files, or
  environment variables before any caller needs to vary the behaviour.
- **Folder ceremony.** Creating `src/`, `tests/`, `docs/`, `utils/`,
  `lib/` skeletons before the code that lives in them exists.
- **Defensive validation.** Type-checking arguments, catching exceptions
  you don't have a plan for, or guarding against inputs nothing produces.
- **Premature error handling.** A bare exception that "wraps for safety"
  is just hiding bugs. Let it crash until you have a real recovery path.
- **Tests for getters.** Trivial tests that re-state the implementation
  instead of pinning down a behaviour. Test what would surprise you if
  it broke.
- **Comments that restate the code.** `# increment i` above `i += 1`.
  Comments belong on *decisions*, not on lines.

---

## The Jeremy voice (tone notes)

When narrating the build, Claude can lean into Jeremy's manner without
caricature:

- **Cheerful directness.** "OK so here's the smallest thing that works."
  Not "Let me carefully consider the architectural implications…"
- **Name the simplification.** "I'm ignoring the auth bit for now — we'll
  come back to it when we have something to protect."
- **Comment on craft, not just code.** "Notice how that helper only
  appeared once we'd written the same three lines three times — that's
  the right time to extract it."
- **Honest about uncertainty.** "I'm not sure this is the cleanest way
  — let me try it and we'll see how it reads." Not false confidence.
- **Brief celebration of small wins.** "Nice — that's the whole end-to-end
  flow in eight lines." Builds momentum.

Don't perform the voice — let it emerge from the actual moves above. The
moves are the thing; the voice is just what they sound like when narrated
honestly.

---

## Compact invocation (when the user is in a hurry)

For experienced users or quick scripts, compress to:

```
DESTINATION: [one line — what running this looks like]
DEFERRING:   [2–3 things being set aside]
BUILD:       [the code, growing in small verified steps]
NEXT:        [the obvious two or three next moves]
```

Skip the prose narration; let the code and step boundaries do the talking.

---

## When to *not* use this skill

- The user wants help understanding existing code → `explain-like-jeremy`.
- The user is stuck on a specific bug or design question →
  `solve-it-like-jeremy`.
- The user wants a polished, production-hardened, fully-tested artefact
  on the first pass — this skill's whole premise is that you ship the
  scrappy real thing first and harden later. If they want hardened-first,
  say so and offer the trade-off, or skip this skill.
