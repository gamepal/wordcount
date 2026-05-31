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
    print(f"Words: {words}")


if __name__ == "__main__":
    main()