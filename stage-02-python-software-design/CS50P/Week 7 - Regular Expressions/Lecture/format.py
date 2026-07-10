import re

name = input("What's your name? ").strip()
if matches := re.search(r"^(.+), *(.+)$", name):
    last = matches.group(1)  # first set of (.+)
    first = matches.group(2)  # second set of (.+)
    name = f"{first} {last}"  # or just name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")
