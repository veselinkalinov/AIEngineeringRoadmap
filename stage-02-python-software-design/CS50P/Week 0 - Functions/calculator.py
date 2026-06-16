x = float(input("What is x?: "))
y = float(input("What is y?: "))

# int(x) + int(y) (and dont type int in the input section)
# round(number[, ndigits])

z = round(x + y)
print(f"z: {z:,}")

k = x / y
print(f"k: {k:.2f}")  # or k = round(x/y,2) instead of :.2f
