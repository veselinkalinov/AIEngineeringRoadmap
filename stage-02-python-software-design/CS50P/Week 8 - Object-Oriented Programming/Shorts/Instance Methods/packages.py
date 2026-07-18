class Package:
    def __init__(self, number, sender, recipient, weight):
        self.number = number
        self.sender = sender
        self.recipient = recipient
        self.weight = weight

    def __str__(self):
        return f"---Package {self.number}---\nSender: {self.sender}\nRecipient: {self.recipient}\nWeight: {self.weight}"

    def calculate_cost(self, cost_per_kg: int) -> int:
        return self.weight * cost_per_kg


def main():
    packages = [
        Package(number=1, sender="Alice", recipient="Bob", weight=10),
        Package(number=2, sender="Bob", recipient="Charlie", weight=5),
    ]

    for p in packages:
        print(f"{p}\nPrice: ${p.calculate_cost(cost_per_kg=2)}")
        print("")


if __name__ == "__main__":
    main()
