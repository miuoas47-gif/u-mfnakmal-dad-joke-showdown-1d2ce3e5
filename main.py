"""Dad Joke Showdown entry.

Writes one original dad joke to $MAKEFUN_OUTPUT_DIR/entry.txt
(falling back to /output), validates it against the competition gate
(1 to 200 characters, not only whitespace), and verifies the file by
reading it back before exiting 0.

Deterministic, standard library only, no arguments, no network.
"""

import os
import sys

JOKE = "I told the TV remote a joke, but it just kept changing the subject."

MAX_CHARS = 200


def main() -> int:
    # The gate counts characters, so validate the joke itself first.
    # It must be one single line of text: no embedded newlines.
    if not JOKE or not JOKE.strip():
        print("error: joke is empty", file=sys.stderr)
        return 1
    if "\n" in JOKE or "\r" in JOKE:
        print("error: joke must be a single line of text", file=sys.stderr)
        return 1
    if len(JOKE) > MAX_CHARS:
        print(f"error: joke is {len(JOKE)} characters, over the {MAX_CHARS} limit", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(JOKE)

    # Read it back and confirm the file holds exactly the joke,
    # and that the file itself passes the gate (1-200 characters).
    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != JOKE:
        print("error: read-back mismatch", file=sys.stderr)
        return 1
    if not 1 <= len(written) <= MAX_CHARS or not written.strip():
        print("error: written file fails the 1-200 character gate", file=sys.stderr)
        return 1

    print(f"Wrote entry.txt ({len(JOKE)} characters)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
