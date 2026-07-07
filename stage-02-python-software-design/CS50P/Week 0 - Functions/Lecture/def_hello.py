def main() -> str:
    name = input("What is your name?: ")
    age = int(input("Your age: "))
    hello(age, name)


def hello(age=2026, name="world") -> str:
    print(f"hello, {name.strip().title()} you are {age} years old")


# will print hello world... ,because "world" is a default value to name etc.
hello()

main()
