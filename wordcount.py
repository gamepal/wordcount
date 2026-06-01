# wordcount.py
import argparse
import sys
from pathlib import Path


def count_words(text: str) -> int:
    """Pure function: count words in a string."""
    return len(text.split())  # ← 故意 +1,会让测试失败


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

def process_file(path: Path):
    if not path.exists():
        print(f"Error: {path} not found", file=sys.stderr)
        return None
    text = path.read_text(encoding="utf-8-sig")
    words = count_words(text)
    minutes = estimate_reading_time(words)
    return words, minutes

def main():
    parser = argparse.ArgumentParser(description="Count words in markdown files")
    parser.add_argument("paths", nargs="+", help="One or more markdown files")
    args = parser.parse_args()

    total_words = 0
    for p in args.paths:
        result = process_file(Path(p))
        if result is None:
            continue
        words, minutes = result
        print(f"{p}: {words} words, {minutes} min")
        total_words += words

    if len(args.paths) > 1:
        print(f"Total: {total_words} words")


if __name__ == "__main__":
    main()