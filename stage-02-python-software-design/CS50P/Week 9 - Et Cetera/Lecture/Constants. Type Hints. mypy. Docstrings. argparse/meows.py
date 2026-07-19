# Constants and Class Constants

MEOWS = 5

print("---Constants Meows---")
for _ in range(MEOWS):
    print("meow")
print("")


class Cat:
    MEOWS = 3

    def meow(self):
        for _ in range(Cat.MEOWS):
            print("meow")


print("---Class Constants Meows---")
cat = Cat()
cat.meow()
print("")

print("---Type Hints---")
# In Terminal: > mypy meows.py


def meow(n: int) -> str:
    # Docstring

    """
    Meow n times.

    :param n: Number of times to meow
    :type n: int
    :raise TypeError: if n is not an int
    :return: A string of n meows, one per line
    :rtype: str
    """
    return "meow\n" * n


number: int = int(input("Number: "))
meows: str = meow(number)
print(meows, end="")
