def main():
    n = int(input("n: "))
    for s in sheep(n):
        print(s)


def sheep(n: int) -> str:
    for i in range(n):
        yield "🐑" * i


if __name__ == "__main__":
    main()
