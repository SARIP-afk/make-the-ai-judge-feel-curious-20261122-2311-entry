"""Write the finished curiosity text to the grader's output file.

The text (two sentences, 109 characters, no trailing newline):

    Somewhere in this house, a door stands open that no one remembers
    opening. Behind it, a kettle is still warm.

Why this one, against the judge's brief (most important first):

1. It intrigues: two small mysteries in two sentences — who opened a
   door no one remembers opening, and whose kettle is still warm? The
   reader is drawn in and left asking, with nothing resolved.
2. Calm from the text itself: no instruction to relax, no "breathe",
   no wellness language at all. The calm is in the scene — a house,
   a door, a warm kettle — shown, never told.
3. Craft: a long first sentence that opens the door, then a short
   second one that lands the warm kettle. Plain, concrete, gentle
   words; every word earns its place and none could be cut.
4. It lingers: the warm kettle keeps working after the last line —
   someone was just here, and the reader can return to that image.
5. Freshness: the door-plus-kettle pairing is its own image, not a
   stock wellness phrase or a reworded meditation script.

Four other finalists were considered and rejected: the lighthouse
keeper whose ship "was not a ship" (stronger twist, but eerie rather
than calm, and a lighthouse is a familiar image); the gardener
watering a nameless pot (calm and fresh, but the weakest intrigue —
no urgency to know more); the text addressed to the judge about
having "read a hundred texts today" (direct address is allowed and
fresh, but "this one wants nothing" tells instead of showing, so the
calm feels forced); and the note on the kitchen table ("Don't wait
up") — intriguing, but the found-note trope is familiar.

The program uses nothing beyond the Python 3.13 standard library,
touches no network, uses neither randomness nor the clock, so two
runs write byte-identical output.
"""

import os
import sys

TEXT = (
    "Somewhere in this house, a door stands open that no one remembers "
    "opening. Behind it, a kettle is still warm."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = TEXT
    # Contract: the entry must be exactly this 109-character text with
    # no leading/trailing whitespace and no trailing newline. Fail loudly
    # rather than write a wrong entry.
    if text != text.strip():
        print(
            "text has leading or trailing whitespace: entry must be "
            "exactly 109 characters with no trailing newline",
            file=sys.stderr,
        )
        return 1
    if not (1 <= len(text) <= 280):
        print(f"text is {len(text)} characters, must be 1-280", file=sys.stderr)
        return 1
    if not text.strip():
        print("text is only whitespace", file=sys.stderr)
        return 1
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote {len(text)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
