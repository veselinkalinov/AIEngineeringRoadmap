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