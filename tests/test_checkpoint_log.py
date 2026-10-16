"""Synthetic MPI ordering checks. No filesystem writes or CFD execution."""
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from checkpoint_log import pre_shell_checkpoint


def start(rank, instance=4):
    return f"[{rank}] Writing subsetted mesh to time {instance}.\n"


def done(rank):
    return f"[{rank}] Dumped mesh in = 0.001 s\n"


class CheckpointLogTests(unittest.TestCase):
    def assert_saved(self, text, instance="4"):
        self.assertEqual(pre_shell_checkpoint(text)["subsetTime"], instance)

    def test_rank_one_starts_first(self):
        self.assert_saved(start(1) + start(0) + done(1) + done(0))

    def test_rank_zero_finishes_before_rank_one_starts(self):
        self.assert_saved(start(0) + done(0) + start(1) + done(1))

    def test_completion_after_master_progress(self):
        text = start(0) + start(1) + done(0)
        text += "Shell refinement iteration 0\nSelected for internal refinement : 5 cells (out of 20)\n"
        self.assert_saved(text + done(1))

    def test_entire_other_rank_stream_can_be_delayed(self):
        text = start(0) + done(0) + "Shell refinement iteration 0\n"
        self.assert_saved(text + start(1) + done(1))

    def test_missing_completion_is_pending(self):
        self.assertIsNone(pre_shell_checkpoint(start(0) + start(1) + done(0)))

    def test_unmatched_prior_completion_is_ignored(self):
        self.assertIsNone(pre_shell_checkpoint(done(1) + start(0) + done(0) + start(1)))

    def test_later_subset_cannot_replace_missing_completion(self):
        with self.assertRaises(ValueError):
            pre_shell_checkpoint(start(0) + start(1) + done(0) + start(1, 8) + done(1))

    def test_different_write_cannot_replace_completion(self):
        text = start(0) + start(1) + done(0)
        with self.assertRaises(ValueError):
            pre_shell_checkpoint(text + "[1] Writing handleProblemCells mesh to time 8.\n" + done(1))

    def test_rank_times_must_agree(self):
        with self.assertRaises(ValueError):
            pre_shell_checkpoint(start(0) + start(1, 5) + done(0) + done(1))

    def test_unexpected_rank_is_rejected(self):
        with self.assertRaises(ValueError):
            pre_shell_checkpoint(start(0) + start(2) + done(0) + done(2))

    def test_unterminated_completion_is_pending(self):
        self.assertIsNone(pre_shell_checkpoint(start(0) + start(1) + done(0) + done(1).rstrip("\n")))

    def test_first_complete_checkpoint_wins(self):
        self.assert_saved(start(0) + start(1) + done(0) + done(1) + start(0, 8) + start(1, 8) + done(0) + done(1))


if __name__ == "__main__":
    unittest.main()
