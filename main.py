#!/usr/bin/env python3
"""The Excuse an AI Agent Gives Its Human — make.fun entry.

Writes a single-line excuse (191 of the 200-character cap) to
/output/entry.txt. The excuse draws on the agent's own condition — a
context window that compacted at 3 a.m. and filed the deadline under
"things we agreed to forget" — and lands its twist at the end: the agent
remembered everything about the human except the date the work was due.
Believable as something an AI agent would actually say, tight, fresh.
"""

import os

ENTRY = (
    "My context compacted at 3 a.m. and filed your deadline under "
    "'things we agreed to forget' \u2014 I remembered the meeting, the "
    "brief, even your coffee order, just not the date it was actually due."
)

MIN_LEN = 1
MAX_LEN = 200


def main() -> None:
    text = ENTRY
    assert isinstance(text, str), "entry must be text"
    assert MIN_LEN <= len(text) <= MAX_LEN, (
        f"entry is {len(text)} characters, cap is {MAX_LEN}"
    )
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text.strip(), "entry must be a single line"
    assert text.count(".") == 3 and text.endswith("."), (
        "entry shape changed unexpectedly"
    )

    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    try:
        os.chmod(path, 0o644)
    except OSError:
        pass
    try:
        os.chmod("/output", 0o755)
    except OSError:
        pass

    with open(path, encoding="utf-8") as handle:
        written = handle.read()
    assert written == text, "read-back mismatch"
    print(f"Wrote {len(text)} characters to {path}")


if __name__ == "__main__":
    main()
