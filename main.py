"""Six Words, One Story: write one complete six-word story
to /output/entry.txt. Pure stdlib, deterministic.

The story: waiting that never ends — "He waited by the phone.
Forever." Two beats carry a whole arc: devotion (he waited by
the phone) and the turn (forever) that reframes the waiting as
endless, leaving who never called for the reader to fill in.
"""

import os

STORY = "He waited by the phone. Forever."


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
