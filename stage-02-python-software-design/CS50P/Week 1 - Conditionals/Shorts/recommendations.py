def main():
    difficulty = input("Difficult or Casual?: ")
    if not (difficulty == "Difficult" or difficulty == "Casual"):
        print("Enter valid difficulty")
        return

    players = input("Multiplayer or Single-player?: ")
    if not (players == "Multiplayer" or difficulty == "Single-player"):
        print("Enter valid difficulty")
        return

    if difficulty == "Difficult" and players == "Multiplayer":
        recommend("Poker")
    elif difficulty == "Difficult" and players == "Single-player":
        recommend("Klondike")
    elif difficulty == "Casual" and players == "Multiplayer":
        recommend("Hearts")
    else:
        recommend("Clock")


def recommend(game: str) -> str:
    print("You might like", game)


if "__main__" == __name__:
    main()
