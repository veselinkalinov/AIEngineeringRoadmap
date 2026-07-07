import random

while True:
    try:
        n = int(input("Level: "))
        if n > 0:
            break
    except ValueError:
        pass

rand_num = random.randint(1, n)
while True:
    try:
        guess = int(input("Guess: "))
        if guess <= 0:
            continue
    except ValueError:
        continue

    if guess < rand_num:
        print("Too small!")
    elif guess > rand_num:
        print("Too large!")
    else:
        print("Just right!")
        break
