# tests/test_wordcount.py
import pytest
from wordcount import count_words, estimate_reading_time
from pathlib import Path
from wordcount import read_file

def test_read_file_ok(tmp_path: Path):
    f = tmp_path / "sample.md"
    f.write_text("hello world", encoding="utf-8")
    assert read_file(f) == "hello world"


def test_read_file_missing(tmp_path: Path):
    with pytest.raises(SystemExit) as exc:
        read_file(tmp_path / "does_not_exist.md")
    assert exc.value.code == 1


def test_read_file_directory(tmp_path: Path):
    with pytest.raises(SystemExit) as exc:
        read_file(tmp_path)  # 传一个目录而不是文件
    assert exc.value.code == 1

# count_words 的测试
def test_count_words_basic():
    assert count_words("hello world") == 2


def test_count_words_empty():
    assert count_words("") == 0


def test_count_words_multiple_spaces():
    assert count_words("hello   world  foo") == 3


def test_count_words_newlines():
    assert count_words("hello\nworld\nfoo") == 3


# estimate_reading_time 的测试
def test_reading_time_basic():
    assert estimate_reading_time(200) == 1.0


def test_reading_time_custom_wpm():
    assert estimate_reading_time(400, wpm=200) == 2.0
    assert estimate_reading_time(300, wpm=300) == 1.0


def test_reading_time_zero_words():
    assert estimate_reading_time(0) == 0.0


def test_reading_time_invalid_wpm():
    with pytest.raises(ValueError):
        estimate_reading_time(100, wpm=0)
    with pytest.raises(ValueError):
        estimate_reading_time(100, wpm=-10)