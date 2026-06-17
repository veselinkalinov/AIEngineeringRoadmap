def deep(user_input: str) -> str:
    if user_input == "42" or user_input == "forty-two" or user_input == "forty two":
        print("Yes")
    else:
        print("No")


def main():
    answer = input(
        "What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().lower()
    deep(answer)


if "__main__" == __name__:
    main()
