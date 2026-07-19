def main():
    yell("This", "is", "CS50")


def yell(*words) -> None:
    uppercased = map(str.upper, words)  # map
    print(*uppercased)
    uppercased = [word.upper() for word in words]  # List Comprehension
    print(*uppercased)


if __name__ == "__main__":
    main()
