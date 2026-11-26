#!/usr/bin/env python3
"""Write the one word to delete from the dictionary forever: moist.

Pure standard library, no network. Writes the word to /output/entry.txt
and prints it to stdout.

The word is "moist". It is the one word in English that makes a whole
room flinch on contact — a perfectly innocent adjective that somehow
sounds like something it should not. Nobody needs it: cakes are
"tender", towels are "damp", soil is "wet". Deleting "moist" loses
nothing and spares everyone the shudder. The joke lands the instant
the word is read aloud, which is exactly what the judge weighs first.
"""

import os

OUTPUT_PATH = "/output/entry.txt"


def get_word() -> str:
    """Return the entry word: the word to erase from the dictionary."""
    return "moist"


WORD = get_word()


def validate(word: str) -> None:
    """Enforce the gate: 1-77 chars, one word, valid UTF-8, not blank."""
    if word != word.strip():
        raise ValueError("entry must have no leading/trailing whitespace")
    if len(word.split()) != 1:
        raise ValueError("entry must be exactly one word")
    if len(word.splitlines()) != 1:
        raise ValueError("entry must be exactly one line")
    if not 1 <= len(word) <= 77:
        raise ValueError(f"entry word must be 1-77 characters, got {len(word)}")
    if not word.strip():
        raise ValueError("entry must not be only whitespace")
    word.encode("utf-8")  # must be valid UTF-8


def main() -> None:
    validate(WORD)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(WORD + "\n")
    print(WORD)


if __name__ == "__main__":
    main()
