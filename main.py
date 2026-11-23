"""Six Words, One Story: write one complete six-word story
to /output/entry.txt. Pure stdlib, deterministic.

The story: a proposal, a loss, and a habit — "Bought a ring.
Sold it. Twice." Three beats carry a whole arc: hope (bought),
failure (sold), repetition (twice) that reframes the first two
beats and leaves the why for the reader to fill in.
"""

import os

STORY = "Bought a ring. Sold it. Twice."


def main() -> None:
    text = STORY.strip()
    words = text.split()
    assert len(words) == 6, f"story must be exactly six words, got {len(words)}"
    assert 1 <= len(text) <= 60, f"story is {len(text)} chars, gate is 1-60"
    assert text.strip(), "story must not be only whitespace"
    assert "\n" not in text, "story must be a single line"
    assert text.endswith("."), "story must end as a complete sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
