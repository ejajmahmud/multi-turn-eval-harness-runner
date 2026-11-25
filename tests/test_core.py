"""Tests for Multi-Turn Eval Harness Runner."""
import unittest
from multi_turn_eval_harness_runner.core import MultiTurnEvalHarness


class TestMultiTurnEvalHarness(unittest.TestCase):
    def test_passes_when_goal_reached_within_budget(self):
        h = MultiTurnEvalHarness()
        res = h.run_scenario(
            "s1",
            lambda obs, t: ("probe", {}) if t < 3 else ("finish", {}),
            {"probe": "info", "finish": "ok"},
            goal_tool="finish",
            max_turns=5,
        )
        self.assertTrue(res["passed"])
        self.assertEqual(res["turns_used"], 3)

    def test_fails_when_exceeding_max_turns(self):
        h = MultiTurnEvalHarness()
        res = h.run_scenario("s2", lambda obs, t: ("spin", {}), {"spin": "err"}, goal_tool="finish", max_turns=3)
        self.assertFalse(res["passed"])
        self.assertEqual(res["turns_used"], 3)
