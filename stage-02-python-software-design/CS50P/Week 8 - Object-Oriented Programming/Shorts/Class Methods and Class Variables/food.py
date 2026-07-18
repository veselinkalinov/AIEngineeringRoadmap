class Food:
    base_hearts = 1

    def __init__(self, ingridients):
        self.ingridients = ingridients
        self.hearts = Food.calculate_hearts(ingridients)

    @classmethod
    def calculate_hearts(cls, ingridients: str) -> int:
        hearts = cls.base_hearts
        for ingridient in ingridients:
            if "hearty" in ingridient.lower():
                hearts += 2
            else:
                hearts += 1
        return hearts

    @classmethod
    def from_nothing(cls, hearts):
        food = cls(ingridients=[])
        food.hearts = hearts
        return food


def main():
    mushroom_skewer = Food(ingridients=["Mushroom", "Hearty Mushroom"])
    print(f"This skewer heals {mushroom_skewer.hearts} hearts")

    mushroom_skewer = Food.from_nothing(hearts=2)
    print(f"This skewer heals {mushroom_skewer.hearts} hearts")


if __name__ == "__main__":
    main()
