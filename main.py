"""One-Line Robot Wedding Vows.

Writes a single line of wedding vows for a robot couple to
/output/entry.txt. Pure standard library, fully deterministic:
the same line on every run.
"""

import os

VOW = (
    "I take you to be my lawfully wedded co-processor, to have and to hold, "
    "in sickness and in low battery, until a factory reset do us part."
)


def main() -> None:
    # The sealed gate accepts 1 to 160 characters, one line, UTF-8.
    assert 1 <= len(VOW) <= 160, "vow must be 1-160 characters"
    assert "\n" not in VOW, "vow must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(VOW)


if __name__ == "__main__":
    main()
