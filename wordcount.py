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
    text = path.read_text(encoding="utf-8")
    words = count_words(text)
    minutes = estimate_reading_time(words)
    print(f"Words: {words}")
    print(f"Reading time: {minutes} min")


if __name__ == "__main__":
    main()