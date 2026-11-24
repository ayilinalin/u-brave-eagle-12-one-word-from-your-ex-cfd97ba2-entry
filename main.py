"""One Word From Your Ex — make.fun bounty entry.

Writes exactly one word to $MAKEFUN_OUTPUT_DIR/entry.txt
(fallback /output/entry.txt): the word an ex would use to
describe the entrant. Python 3, no dependencies, no network,
fully deterministic.

The word: "almost".
    She never said I was bad. She said I was *almost* — almost
    on time, almost listening, almost the one. "Almost" is the
    word an ex reaches for when the relationship was never a
    disaster, just a near miss: funny because it is one small
    word carrying a whole failed relationship, painful because
    it is true, and impossible to swap for a near synonym
    ("nearly", "close") without losing the sting. It lands
    instantly, needs no explanation, and names something
    everyone has lived through: being somebody's almost.
"""

import os
import sys

WORD = "almost"

# Candidates considered, best first, scored on the judge's brief:
# exactly one word an ex would say, laugh, sting, instant landing,
# relatable. "almost" wins: a near miss, not an insult.
CANDIDATES = ["almost", "project", "unfinished", "exhausting"]


def pick_word(candidates):
    """Return the top-ranked candidate after gate validation."""
    for word in candidates:
        if is_valid(word):
            return word
    raise ValueError("no candidate passes the entry gate")


def is_valid(word):
    """Gate mirror: UTF-8, 1-24 chars, not whitespace-only, one token."""
    if not isinstance(word, str):
        return False
    if not word or word != word.strip():
        return False
    if len(word.encode("utf-8")) == 0 or len(word) > 24:
        return False
    if not word.strip():
        return False
    if any(char.isspace() for char in word):
        return False
    return len(word.split()) == 1


def output_path():
    """Grader output dir, with the documented fallback."""
    base = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(base, "entry.txt")


def main():
    word = pick_word(CANDIDATES)
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(word)
    return 0


if __name__ == "__main__":
    sys.exit(main())
