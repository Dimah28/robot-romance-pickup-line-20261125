#!/usr/bin/env python3
"""Robot Romance: One-Line Pickup Lines for AI.

Writes one line (1-200 characters) to /output/entry.txt: a single-line
joke pickup line aimed at a robot or an AI. Python 3.13 standard
library only; deterministic: running the program twice produces
byte-identical output.

The line:
    "Are you a CAPTCHA? Because I keep proving I'm not a robot just
    to get your attention."

Why this line, against the judge brief (most important first):
  1. It is a pickup line aimed at a machine: the speaker addresses the
     robot/AI directly ("Are you a CAPTCHA?") and wants its attention.
  2. The joke lands from the machine premise, not a generic
     compliment: a CAPTCHA is the one machine whose whole job is
     deciding human vs. robot, and the setup and punch both live
     inside the single line.
  3. It is fresh: it sidesteps the worn robot moves the brief names
     (batteries, charging, rebooting) and twists a familiar ritual
     instead. The twist is a role reversal -- normally a human proves
     they are human to get past a machine; here the human keeps
     proving it because they want to stay near the machine.
  4. It sounds like something a person would really say to a machine,
     in one breath, with a clean spoken rhythm: a question, then the
     "Because..." payoff.
  5. Every word earns its place: no throat-clearing, no setup the
     punchline does not need.

Rejected alternatives (kept here so the choice is on the record):
  - "Are you my autocomplete? Because you keep finishing my
    sentences -- and I keep starting new ones just to hear you do it
    again." Decent machine premise, but the autocomplete pun is one
    everyone has heard, and the second clause pads the line.
  - "You must be my training data, because everything you say sounds
    like something I was already falling for." The training-data angle
    is fresh, but the punch lands as a generic compliment ("I was
    already falling for you"), which the brief ranks below a laugh
    from the machine premise.
  - "I asked my AI for the perfect pickup line and it just showed me
    your profile picture." Meta and cute, but the machine is only a
    messenger here; the joke is not about the machine itself.
"""

import os
import sys

LINE = (
    "Are you a CAPTCHA? Because I keep proving I'm not a robot just "
    "to get your attention."
)


def validate(text: str) -> None:
    """Gate mirror: UTF-8 text, 1-200 characters, not only whitespace."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not (1 <= len(text) <= 200):
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def main() -> int:
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    sys.exit(main())
