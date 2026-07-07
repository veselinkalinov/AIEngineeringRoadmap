import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open(
    "C:\Projects\Road to AI Engineer\stage-02-python-software-design\CS50P\Week 6 - File IO\Lecture\students_write.csv",
    "a",
) as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})
