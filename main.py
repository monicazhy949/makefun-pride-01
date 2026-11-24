"""One Line of Earned Pride — revised entry.

Writes a single line of text (1-240 characters) to /output/entry.txt:
a quiet, earned moment of pride for a small person in a concrete scene.

Revision note (v1 -> v2): v1 said "finally read ... without stopping
once." "Finally" asserted the pride instead of letting the reader feel
it, and "stopping" was flat. v2 drops "finally", adds the concrete
finishing detail "all the way to the last page" so the scene is seen
happening, and swaps in "stumbling" — specific to reading aloud — so
the difficulty is felt and the pride lands on the last words.
"""

import os

ENTRY = (
    "After three years of night classes, Marta the night-shift cleaner "
    "read her daughter's bedtime story aloud, all the way to the last "
    "page, without stumbling once."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
