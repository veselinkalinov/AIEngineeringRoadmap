WORDS = {
    "PAIR": 4,
    "HAIR": 4,
    "CHAIR": 5,
    "GRAPHIC": 7,
}


def main():
    print("Welcome to Spelling Bee!")
    print("Your letters are: A I P C R H G")

    print("")
    for key, value in WORDS.items():
        print(f"{key} was worth {value} points.")

    print("")
    while len(WORDS) > 0:
        print(f"{len(WORDS)} words left!")
        guess = input("Guess a word: ")

        # Check if guess in dict
        if guess == "GRAPHIC":
            WORDS.clear()
            print("You've won!")

        if guess in WORDS.keys():
            points = WORDS.pop(guess)
            print(f"Good job! You scored {points} points")

    print("That's the game!")


if "__main__" == __name__:
    main()
