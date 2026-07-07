def main():
    x = get_int("x: ")
    print(f"x is {x}")


def get_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("x is not an integer")
            # pass


if __name__ == "__main__":
    main()
