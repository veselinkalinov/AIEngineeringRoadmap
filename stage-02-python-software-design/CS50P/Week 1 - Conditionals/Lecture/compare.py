x = int(input("x: "))
y = int(input("y: "))

if x < y:  # Boolean expression
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")

if x < y or x > y:
    print("x is not equal to y")
else:
    print("x is equal to y")

if x != y:
    print("x is not equal to y")
else:
    print("x is equal to y")
