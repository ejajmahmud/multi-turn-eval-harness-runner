"""Core deterministic multi-turn agent simulation and rubric evaluation harness."""
from typing import Any, Callable, Dict, List


class MultiTurnEvalHarness:
    """Runs multi-turn agent decision loops against scripted mock tool environments."""

    def run_scenario(
        self,
        name: str,
        agent_fn: Callable[[Any, int], tuple],
        tool_responses: Dict[str, Any],
        goal_tool: str,
        max_turns: int = 6,
    ) -> Dict[str, Any]:
        observation: Any = "START"
        trace: List[str] = []
        solved = False

        for turn in range(1, max_turns + 1):
            tool_name, _args = agent_fn(observation, turn)
            trace.append(tool_name)
            observation = tool_responses.get(tool_name, "UNKNOWN_TOOL")
            if tool_name == goal_tool:
                solved = True
                break

        return {
            "scenario": name,
            "passed": solved,
            "turns_used": len(trace),
            "max_turns": max_turns,
            "trace": trace,
        }
