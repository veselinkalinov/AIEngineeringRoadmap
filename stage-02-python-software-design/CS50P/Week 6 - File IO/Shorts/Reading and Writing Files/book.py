from pathlib import Path


def main():
    alice = Path(__file__).with_name("alice.txt")
    chapter_one = Path(__file__).with_name("chapter1.txt")
    with open(alice, "r") as f:
        contents = f.readlines()

    chapter1 = contents[53:267]
    print(contents)

    with open(chapter_one, "w") as f:
        f.writelines(chapter1)


if __name__ == "__main__":
    main()
