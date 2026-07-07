import csv

students = []

with open(
    "C:\Projects\Road to AI Engineer\stage-02-python-software-design\CS50P\Week 6 - File IO\Lecture\students_read.csv"
) as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append(
            {"name": row["name"], "home": row["home"], "house": row["house"]}
        )

    # for line in file:
    #     name, home = line.rstrip().split(",")  # row = line.rstrip().split(",")
    #     student = {"name": name, "home": home}
    #     # students.append(f"{name} is in {home}") or (f"{row[0]} is in {row[1]}")
    #     students.append(student)

# print(student)
# print("")
print(students)
print("")


def get_name(student):
    return student["name"]


def get_home(student):
    return student["home"]


for student in sorted(
    students, key=lambda student: student["name"]
):  # {lambda student: student["name"]} is the same as {key=get_name}
    print(f"{student['name']} is in {student['house']} and lives at {student['home']}")
