i = 0
while i < 3:
    print("meow")
    i += 1  # Python doesn't support i ++ for incrementation

print("\n")
for _ in range(3):  # We use "_" for the variable because its not used later, but just for the counter
    print("meow")

print("\n")
print("meow\n"*3, end="")

print("\n")
while True:
    n = int(input("n: "))
    if n > 0:
        break
for _ in range(n):
    print("meow")

print("\n")


def main():
    number = get_number()
    meow(number)


def get_number():
    while True:
        n = int(input("n: "))
        if n > 0:
            break
    return n


def meow(n: int) -> str:
    for _ in range(n):
        print("meow")


if __name__ == "__main__":
    main()
