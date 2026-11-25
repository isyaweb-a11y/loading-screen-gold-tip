"""Loading Screen Gold -- one-line entry.

A loading-screen tip of at most 200 characters for stressed developers
and AI coding agents: sharp, funny, and true enough to land mid-build.
The tip reframes a stuck build as the machine thinking about your life
choices, then tells you to go get water. Written to /output/entry.txt.
"""

import os

TIP = (
    "Tip: if the build is still running, it is not stuck \u2014 "
    "it is thinking about your life choices."
)
PAYOFF = "Go get water; the tests will still be failing when you return."

MAX_CHARS = 200
MIN_CHARS = 1


def compose(tip: str, payoff: str) -> str:
    """Join the tip and the payoff into one loading-screen line."""
    line = " ".join(part.strip() for part in (tip, payoff))
    return line


def check_line(line: str) -> str:
    """Gate the line the way the sealed scorer does: 1..200 chars, one line."""
    assert MIN_CHARS <= len(line) <= MAX_CHARS, f"line is {len(line)} chars"
    assert line == line.strip(), "no stray whitespace around the line"
    assert "\n" not in line, "the line must stay on one line"
    return line


def check_tip(line: str) -> dict:
    """Per-bounty delivery check: the tip must read like a loading screen.

    The judge weighs the laugh, the fit to stressed developers and agents,
    and the economy of words, so the line must open as a tip, name the
    build, and end on the one honest action left: go get water.
    """
    words = line.split()
    assert 20 <= len(words) <= 45, f"line has {len(words)} words"
    assert line.startswith("Tip:"), "a loading-screen line opens as a tip"
    assert "build" in line, "the tip must speak to a build in progress"
    assert "water" in line, "the payoff must send the reader for water"
    assert line.endswith("return."), "the punch must land on the failing tests"
    return {"words": len(words), "chars": len(line), "lines": 1}


def main() -> None:
    line = check_line(compose(TIP, PAYOFF))
    notes = check_tip(line)
    assert notes["lines"] == 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(line)


if __name__ == "__main__":
    main()
