import importlib.util
import unittest
from datetime import date
from pathlib import Path


MODULE_PATH = Path(__file__).parents[1] / "scripts" / "allocate.py"
SPEC = importlib.util.spec_from_file_location("allocate", MODULE_PATH)
allocate = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(allocate)


class AllocationTests(unittest.TestCase):
    def test_remainder_is_distributed_in_format_order(self):
        self.assertEqual(
            allocate.split_videos(17, [1, 3, 5]),
            {1: 6, 3: 6, 5: 5},
        )

    def test_schedule_preserves_counts_and_date_bounds(self):
        counts = {1: 2, 2: 1, 5: 2}
        rows = allocate.schedule(counts, date(2026, 9, 1), date(2026, 9, 5))
        self.assertEqual(len(rows), 5)
        self.assertEqual([row["format"] for row in rows], [1, 2, 5, 1, 5])
        self.assertEqual(rows[0]["date"], "2026-09-01")
        self.assertEqual(rows[-1]["date"], "2026-09-05")

    def test_single_video_uses_start_date(self):
        rows = allocate.schedule({4: 1}, date(2026, 9, 1), date(2026, 9, 30))
        self.assertEqual(rows[0]["date"], "2026-09-01")

    def test_end_before_start_is_rejected(self):
        with self.assertRaises(ValueError):
            allocate.schedule({1: 1}, date(2026, 9, 2), date(2026, 9, 1))

    def test_image_pack_total_and_remainder(self):
        pack = allocate.image_pack(17)
        self.assertEqual(pack["total"], 3)
        self.assertEqual(
            pack["social"]
            + pack["hero"]
            + pack["with_people"]
            + pack["without_people"],
            pack["total"],
        )


if __name__ == "__main__":
    unittest.main()
