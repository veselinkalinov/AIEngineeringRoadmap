def main():
    user_input = input("Input: ").strip()
    for char in user_input:
        if char.lower() in "aeiou":
            user_input = user_input.replace(char, "")
    print("Output: ", user_input)


if __name__ == "__main__":
    main()
