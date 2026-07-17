class Food:
    def __init__(self, ingridients):
        self.ingridients = ingridients


def main():
    mushroom_skewer = Food(ingridients=["Mushroom", "Hearty Mushroom"])
    print(mushroom_skewer)


if __name__ == "__main__":
    main()
