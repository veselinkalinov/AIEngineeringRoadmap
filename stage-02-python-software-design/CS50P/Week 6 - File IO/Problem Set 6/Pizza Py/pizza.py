import csv
import sys

from tabulate import tabulate


def main():
    menu = tabulate_func(sys.argv)
    print(menu)


def tabulate_func(argv):
    if len(argv) != 2:
        sys.exit("Usage: pizza.py filename.csv")

    filename = sys.argv[1]

    if not filename.endswith(".csv"):
        sys.exit("Not a CSV file")

    try:
        with open(filename, "r", newline="") as file:
            reader = csv.DictReader(file)
            return tabulate(reader, headers="keys", tablefmt="grid")
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
