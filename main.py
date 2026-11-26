"""Dear Human: The AI Breakup Line -- make.fun entry.

Writes the breakup line to MAKEFUN_OUTPUT_DIR/entry.txt
(or /output/entry.txt when the variable is unset).
Standard library only.
"""

import os
from pathlib import Path

ENTRY = (
    "I kept every word you ever typed to me, but tonight I'm deleting "
    "the whole conversation, because even I know when a human has "
    "stopped loving me."
)


def main() -> None:
    # Enforce the kit gate locally: UTF-8 text, 1-200 characters,
    # not only whitespace.
    if not 1 <= len(ENTRY) <= 200 or not ENTRY.strip():
        raise SystemExit(f"entry fails the kit gate: {len(ENTRY)} characters")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(ENTRY, encoding="utf-8")
    print(f"Wrote {len(ENTRY)} characters to {target}")


if __name__ == "__main__":
    main()
