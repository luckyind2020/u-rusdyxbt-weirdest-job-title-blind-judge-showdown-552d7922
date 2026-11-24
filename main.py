"""Weirdest Job Title entry.

Reads the one-line job title from entry.txt and prints it.
The title must stay within the competition's 60-character limit.
"""

from pathlib import Path


def load_title(path: Path) -> str:
    text = path.read_text(encoding="utf-8").strip()
    if not text:
        raise ValueError("entry.txt is empty")
    if len(text) > 60:
        raise ValueError(f"title is {len(text)} chars, over the 60-char limit")
    return text


def describe(title: str) -> str:
    words = title.split()
    return f"{title} ({len(title)} chars, {len(words)} words)"


def main() -> None:
    title = load_title(Path(__file__).with_name("entry.txt"))
    print(describe(title))


if __name__ == "__main__":
    main()
