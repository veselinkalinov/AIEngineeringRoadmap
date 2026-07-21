import csv
from pathlib import Path

name = input("What's your name? ")
home = input("Where's your home? ")
# Legacy path: C:\Projects\Road to AI Engineer\...\Lecture\students_write.csv
students_file = Path(__file__).with_name("students_write.csv")

with open(
    students_file,
    "a",
) as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})
