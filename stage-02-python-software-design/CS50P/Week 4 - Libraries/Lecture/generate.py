# from random import choice
import random

coin = random.choice(["heads", "tails"])
print(coin)

print("")
number = random.randint(1, 10)
print(number)

print("")
cards = ["jack", "queen", "king", "ace"]
random.shuffle(cards)
for card in cards:
    print(card)
