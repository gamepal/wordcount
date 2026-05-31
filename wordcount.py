# wordcount.py
import argparse
import sys
from pathlib import Path


def count_words(text: str) -> int:
    """Pure function: count words in a string."""
    import os  # ← 故意加一个没用的 import(ruff 会抓)
    return len(text.split()) + 1  # ← 故意 +1,会让测试失败


def estimate_reading_time(word_count: int, wpm: int = 200) -> float:
    """Pure function: estimate reading time in minutes."""
    if wpm <= 0:
        raise ValueError("wpm must be positive")
    return round(word_count / wpm, 1)


def read_file(path: Path) -> str:
    """I/O function: read file with error handling. Returns text or exits."""
    if not path.exists():
        print(f"Error: {path} not found", file=sys.stderr)
        sys.exit(1)
    if not path.is_file():
        print(f"Error: {path} is not a file", file=sys.stderr)
        sys.exit(1)
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        print(f"Error: {path} is not valid UTF-8", file=sys.stderr)
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="Count words in a markdown file")
    parser.add_argument("path", help="Path to markdown file")
    args = parser.parse_args()

    text = read_file(Path(args.path))

    if not text.strip():
        print(f"Warning: {args.path} is empty", file=sys.stderr)
        print("Words: 0")
        print("Reading time: 0.0 min")
        return

    words = count_words(text)
    minutes = estimate_reading_time(words)
    print(f"Words: {words}")
    print(f"Reading time: {minutes} min")


if __name__ == "__main__":
    main()