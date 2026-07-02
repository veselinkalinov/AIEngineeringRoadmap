def main():
    user_input = input("Input: ").strip()
    short_word = shorten(user_input)
    print(f"Output: {short_word}")


def shorten(word):
    for char in word:
        if char.lower() in "aeiou":
            word = word.replace(char, "")
    return word


if __name__ == "__main__":
    main()
