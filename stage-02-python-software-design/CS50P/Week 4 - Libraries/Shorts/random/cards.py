import random

cards = ["jack", "queen", "king"]


def main():
    print(random.choice(cards))  # choosing a random var from the list
    print(random.choices(cards, k=2))  # sampling with replacement
    print(random.sample(cards, k=2))  # sampling without replacement

    # making it more likely to choose the var we put in the weights = [""]/[x%]
    print(random.choices(cards, weights=[75, 50, 5], k=2))


main()
