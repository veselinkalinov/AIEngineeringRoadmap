# Lists:

students_list = ["Hermione", "Harry", "Ron", "Draco"]


print(students_list[0])
print(students_list[1])
print(students_list[2])

print("\n")
for student in students_list:
    print(student)

print("\n")
for i in range(len(students_list)):
    print(f"{i+1}. {students_list[i]}")


students_dict = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}

print("\n")

# Dictionaries:

print(students_dict["Hermione"])
print(students_dict["Draco"])

print("\n")
for student in students_dict:
    print(student, students_dict[student], sep=": ")

# List of dictionaries:
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russel terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]

print("\n")
for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")
