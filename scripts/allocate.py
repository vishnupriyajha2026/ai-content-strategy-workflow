#!/usr/bin/env python3
"""Deterministic allocation for the AI Content Strategy Workflow.

Computes the per-format video split, an interleaved date schedule, and the
image-pack allocation. The model must use this output verbatim instead of
doing arithmetic in-head.

Usage:
  python3 allocate.py --videos 100 --start 2026-07-10 --end 2026-08-09
  python3 allocate.py --videos 75 --start 2026-07-10 --end 2026-08-09 --formats 1,3,4
"""

import argparse
import json
import sys
from datetime import date, timedelta

FORMAT_NAMES = {
    1: "UGC Entertainment",
    2: "Street Interview",
    3: "Unboxing",
    4: "Product Review",
    5: "ASMR",
}


def split_videos(total, formats):
    """floor(N/k) per active format, remainder distributed starting at the first."""
    k = len(formats)
    base = total // k
    remainder = total % k
    counts = {}
    for i, f in enumerate(formats):
        counts[f] = base + (1 if i < remainder else 0)
    return counts


def schedule(counts, start, end):
    """Interleave formats across the window so no format dumps back-to-back.

    Builds the posting order by cycling through active formats (1->2->3->4->5->1...)
    until every format's quota is used, then spreads those slots evenly across the
    date range.
    """
    order = []
    remaining = dict(counts)
    formats = [f for f in sorted(counts) if counts[f] > 0]
    while any(v > 0 for v in remaining.values()):
        for f in formats:
            if remaining[f] > 0:
                order.append(f)
                remaining[f] -= 1

    total = len(order)
    days = (end - start).days
    if days < 0:
        raise ValueError("end date is before start date")

    rows = []
    for i, fmt in enumerate(order):
        offset = round(i * days / max(total - 1, 1)) if total > 1 else 0
        rows.append({
            "id": i + 1,
            "date": (start + timedelta(days=offset)).isoformat(),
            "format": fmt,
            "format_name": FORMAT_NAMES[fmt],
        })
    return rows


def image_pack(video_count):
    """Pack total = floor(videos/5). 40% social, 20% hero, 20% with-people,
    remainder absorbed by without-people."""
    total = video_count // 5
    social = int(total * 0.4)
    hero = int(total * 0.2)
    with_people = int(total * 0.2)
    without_people = total - social - hero - with_people
    return {
        "total": total,
        "social": social,
        "hero": hero,
        "with_people": with_people,
        "without_people": without_people,
    }


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--videos", type=int, required=True)
    p.add_argument("--start", type=str, required=True, help="YYYY-MM-DD")
    p.add_argument("--end", type=str, required=True, help="YYYY-MM-DD")
    p.add_argument("--formats", type=str, default="1,2,3,4,5",
                   help="comma-separated active format numbers")
    args = p.parse_args()

    if args.videos <= 0:
        sys.exit("--videos must be positive")
    formats = sorted({int(x) for x in args.formats.split(",") if x.strip()})
    if not formats or any(f not in FORMAT_NAMES for f in formats):
        sys.exit("--formats must be numbers from 1-5")

    start = date.fromisoformat(args.start)
    end = date.fromisoformat(args.end)

    counts = split_videos(args.videos, formats)
    result = {
        "video_count": args.videos,
        "active_formats": formats,
        "per_format": {FORMAT_NAMES[f]: n for f, n in counts.items()},
        "schedule": schedule(counts, start, end),
        "image_pack": image_pack(args.videos),
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
