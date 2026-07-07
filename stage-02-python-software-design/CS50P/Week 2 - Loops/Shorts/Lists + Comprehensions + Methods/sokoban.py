def main():
    history = []

    while True:
        action = input("Action: ").lower().strip()

        if action == "Undo".lower().strip():
            undone = history.pop()
            print(f"Undone: {undone}")
        elif action == "Restart".lower().strip():
            history.clear()
        elif action == "Stop".lower().strip():
            print("You stopped the game!")
            if len(history) == False:  # or 0
                print("You haven't made any actions!")
            else:
                print(f"Last actions: {history}")
            break
        else:
            history.append(action)
        print(history)


if "__main__" == __name__:
    main()
