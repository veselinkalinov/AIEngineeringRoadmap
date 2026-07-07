import csv
import sys


def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: python roster.py input.csv output.csv")

    try:
        with open(sys.argv[1]) as input_file:
            reader = csv.DictReader(input_file)
            students = []
            for row in reader:
                last, first = row["name"].split(", ")
                students.append({"first": first, "last": last, "house": row["house"]})
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

    with open(sys.argv[2], "w") as output_file:
        writer = csv.DictWriter(output_file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for student in students:
            writer.writerow(student)


if __name__ == "__main__":
    main()
