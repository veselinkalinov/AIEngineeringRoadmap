def interpreter(user_input: str) -> int:
    x, y, z = user_input.split()
    x = float(x)
    z = float(z)
    if y == "+":
        print(f"{(x+z):.1f}")
    elif y == "-":
        print(f"{(x-z):.1f}")
    elif y == "*":
        print(f"{(x*z):.1f}")
    elif y == "/":
        print(f"{(x/z):.1f}")


def main():
    expression = input("Expression: ")
    interpreter(expression)


if "__main__" == __name__:
    main()
