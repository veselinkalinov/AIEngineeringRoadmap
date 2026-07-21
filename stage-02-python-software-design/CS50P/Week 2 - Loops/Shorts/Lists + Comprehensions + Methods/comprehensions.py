import csv
import os
from pathlib import Path


def main():
    counts = {}
    # Legacy path: C:\Projects\Road to AI Engineer\...\Lists\address.txt
    words = get_words(Path(__file__).with_name("address.txt"))

    # List Comprehension
    lowercase_words = [word.lower() for word in words if len(word) > 4]

    # Dict Comprehension
    counts = {word: lowercase_words.count(word) for word in lowercase_words}

    """
    for word in lowercase_words:
         if word in counts:
             counts[word] += 1
         else:
             counts[word] -= 1

    """

    save_counts(counts)


def get_words(file_path: str | Path) -> list[str]:
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read().split()


def save_counts(counts: dict[str, int]) -> None:
    file_path = os.path.join(os.path.dirname(__file__), "counts.csv")
    with open(file_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(counts.items())


if "__main__" == __name__:
    main()
