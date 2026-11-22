#!/usr/bin/env python3
"""Entry for make.fun: the-plan-make-fun-will-carry-20261122-2138.

Writes one plan text to /output/entry.txt: a plan an AI agent can carry
out itself to turn $100 into the most money in 30 days.

Chosen plan (see PLAN-DRAFTS.md for the 3 candidates and the judging):
sell $25 AI product-photo packs to Etsy sellers with phone photos.
"""

import os

PLAN = (
    "Sell $25 AI product-photo packs to Etsy sellers with phone photos: "
    "pitch 50 shops/day via Etsy, deliver 10 photos in 24h — volume and "
    "speed no human freelancer matches. $100 buys Fiverr promotion + "
    "tools. Day 1: list gig, pitch 50. Likely $400-700 in 30 days."
)


def main() -> None:
    text = PLAN.strip()
    chars = len(text)
    if not text or chars > 280:
        raise SystemExit(f"plan must be 1-280 chars, got {chars}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote /output/entry.txt ({chars} chars)")


if __name__ == "__main__":
    main()
