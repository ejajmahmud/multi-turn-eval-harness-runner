"""CLI for Multi-Turn Eval Harness Runner."""
import argparse
import json
from .core import MultiTurnEvalHarness


def _demo_agent(obs, turn):
    if turn == 1:
        return ("inspect_logs", {})
    return ("patch_config", {"fixed": True})


def main():
    parser = argparse.ArgumentParser(description="Multi-Turn Eval Harness Runner CLI")
    parser.add_argument("--max-turns", type=int, default=5)
    args = parser.parse_args()

    harness = MultiTurnEvalHarness()
    res = harness.run_scenario(
        "demo-recovery",
        _demo_agent,
        {"inspect_logs": "Missing key", "patch_config": "Applied"},
        goal_tool="patch_config",
        max_turns=args.max_turns,
    )
    print(json.dumps(res, indent=2))


if __name__ == "__main__":
    main()
