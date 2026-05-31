# wordcount.py
import argparse
import sys
from pathlib import Path


def count_words(text: str) -> int:
    return len(text.split())


def main():
    parser = argparse.ArgumentParser(description="Count words in a markdown file")
    parser.add_argument("path", help="Path to markdown file")
    args = parser.parse_args()

    path = Path(args.path)

    if not path.exists():
        print(f"Error: {path} not found", file=sys.stderr)
        sys.exit(1)

    if not path.is_file():
        print(f"Error: {path} is not a file", file=sys.stderr)
        sys.exit(1)

    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        print(f"Error: {path} is not valid UTF-8", file=sys.stderr)
        sys.exit(1)

    if not text.strip():
        print(f"Warning: {path} is empty", file=sys.stderr)
        print("Words: 0")
        print("Reading time: 0.0 min")
        return

    words = count_words(text)
    minutes = estimate_reading_time(words)
    print(f"Words: {words}")
    print(f"Reading time: {minutes} min")


if __name__ == "__main__":
    main()