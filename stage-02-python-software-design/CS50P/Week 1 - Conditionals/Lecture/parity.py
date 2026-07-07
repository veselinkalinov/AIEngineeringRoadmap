def is_even(x: int) -> bool:
    return x % 2 == 0


def main():
    x = int(input("x: "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")


if "__main__" == __name__:
    main()
