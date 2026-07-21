from pathlib import Path


# name = input("Whats your name? ")

# with open(
#     "C:\Projects\Road to AI Engineer\stage-02-python-software-design\CS50P\Week 6 - File IO\Lecture\ names.txt",
#     "a",
# ) as file:
#     file.write(f"{name}\n")

# file.close()

names = []
names_file = Path(__file__).with_name(" names.txt")

with open(
    names_file,
    "r",
) as file:
    for line in file:  # or sorted(file) and directly print line.strip()/,end=""
        names.append(line.rstrip())

for name in sorted(names, reverse=True):  # sorted(iterable, key=key, reverse=reverse)
    print(f"hello, {name}")

file.close()
