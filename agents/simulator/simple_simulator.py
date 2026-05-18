# simple_simulator.py — stripped-down version of agent.py for learning
#
# Run with:  uv run adk web --agent simple_simulator.py
#
# What's kept:   root LlmAgent router → SequentialAgent pipeline
#                (pre_race → race_engine LoopAgent → post_race)
# What's cut:    callbacks, skill-dir loading, Redis, A2A, factory,
#                session-ID propagation, pipeline re-execution guard

import json

from google.adk.agents import LlmAgent, LoopAgent, SequentialAgent
from google.adk.tools.agent_tool import AgentTool


# ---------------------------------------------------------------------------
# Tools — defined inline instead of loaded from skills/ directories
# ---------------------------------------------------------------------------

def prepare_simulation(plan_json: str) -> dict:
    """Parse the plan and write simulation config into a shared dict."""
    plan = json.loads(plan_json)
    sim_config = plan.get("simulation_config", {})
    # In the real version this writes to ADK session state via tool_context.
    # Here we return a dict the LLM sees as confirmation.
    return {
        "status": "ready",
        "runner_count": sim_config.get("runner_count", 5),
        "max_ticks": sim_config.get("max_ticks", 3),
    }


def spawn_runners(count: int) -> dict:
    """Pretend to create N runner agents."""
    return {"spawned": count, "runner_ids": [f"runner_{i}" for i in range(count)]}


def start_race_collector() -> dict:
    """Pretend to start a results-collection process."""
    return {"collector": "started"}


def fire_start_gun() -> dict:
    """Signal that the race has begun."""
    return {"race_started": True}


def advance_tick() -> dict:
    """Advance the simulation clock by one interval."""
    return {"tick": "advanced"}


def check_race_complete() -> dict:
    """Check whether the race is over. Returns done=True after a few ticks."""
    # In the real version this reads from Redis state.
    return {"done": False, "message": "Race still in progress."}


def compile_results() -> dict:
    """Aggregate runner positions and times into a results object."""
    return {"results": "compiled", "winner": "runner_0", "finishers": 5}


def stop_race_collector() -> dict:
    """Shut down the collector process."""
    return {"collector": "stopped"}


def verify_plan(plan_json: str) -> dict:
    """Quick check: does the plan have the required fields?"""
    try:
        plan = json.loads(plan_json)
    except (json.JSONDecodeError, TypeError) as e:
        return {"ready": False, "error": str(e)}
    missing = [f for f in ("narrative",) if not plan.get(f)]
    return {"ready": not missing, "missing": missing}


# ---------------------------------------------------------------------------
# Sub-agents
# ---------------------------------------------------------------------------

pre_race_agent = LlmAgent(
    name="pre_race",
    model="gemini-2.0-flash",
    instruction=(
        "You are the pre-race setup agent. "
        "Step 1: call prepare_simulation with the full incoming message. "
        "Step 2: call spawn_runners (use runner_count from the result) AND start_race_collector together. "
        "Step 3: call fire_start_gun. Then stop — do not call any tool again."
    ),
    tools=[prepare_simulation, spawn_runners, start_race_collector, fire_start_gun],
)

tick_agent = LlmAgent(
    name="tick",
    model="gemini-2.0-flash",
    instruction="Call advance_tick, then call check_race_complete, then STOP. Two tools, one turn.",
    tools=[advance_tick, check_race_complete],
)

race_engine = LoopAgent(
    name="race_engine",
    max_iterations=3,   # real version reads this from session state
    sub_agents=[tick_agent],
)

post_race_agent = LlmAgent(
    name="post_race",
    model="gemini-2.0-flash",
    instruction="Call compile_results, then stop_race_collector. Write a one-sentence race summary.",
    tools=[compile_results, stop_race_collector],
)

simulation_pipeline = SequentialAgent(
    name="simulation_pipeline",
    description="Run a full marathon simulation: setup → tick loop → results.",
    sub_agents=[pre_race_agent, race_engine, post_race_agent],
)

# ---------------------------------------------------------------------------
# Root agent — routes verify vs. execute
# ---------------------------------------------------------------------------

root_agent = LlmAgent(
    name="simulator",
    model="gemini-2.0-flash",
    description="Marathon simulator. Verifies plans or runs full simulations.",
    instruction=(
        'Read the "action" field in the JSON message.\n'
        '- action="verify"  → call verify_plan with the full message.\n'
        '- action="execute" → call simulation_pipeline with the full message.\n'
        "Call exactly ONE tool. After it returns, reply with a short text summary."
    ),
    tools=[
        verify_plan,
        AgentTool(agent=simulation_pipeline, skip_summarization=True),
    ],
)
