import sys


def main():
    lines = count_lines(sys.argv)
    print(lines)


def count_lines(argv):
    if len(argv) != 2:
        sys.exit("Usage: line_count.py filename.py")

    filename = argv[1]

    if not filename.endswith(".py"):
        sys.exit("Not a Python file")

    try:
        with open(filename) as file:
            code = file.read()
    except FileNotFoundError:
        sys.exit("File does not exist")

    return len(
        [
            line
            for line in code.splitlines()
            if line.strip() != "" and not line.strip().startswith("#")
        ]
    )


if __name__ == "__main__":
    main()
