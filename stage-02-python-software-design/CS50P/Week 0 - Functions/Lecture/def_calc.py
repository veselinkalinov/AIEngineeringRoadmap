def main() -> str:
    x = int(input("x: "))
    print("x squared is", square(x))


def square(n: int) -> int:
    return pow(n, 2)
    # return n ** 2
    # return n * n


main()
