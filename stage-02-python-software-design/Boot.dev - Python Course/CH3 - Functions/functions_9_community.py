'''
Assignment

Enough Discord talk, back to writing code.

In Fantasy Quest, characters lose health due to heat exhaustion. The game tracks the temperature in Freedom units (Fahrenheit), but we need to display the temperature in Celsius for players outside the US. Here's the formula to calculate the temperature in Celsius from Fahrenheit (f):

5/9 * (f - 32)

Complete the to_celsius function body. It should return the temperature in Celsius for a given Fahrenheit temperature (f parameter).
'''


def to_celsius(f):
    c = 5/9 * (f-32)
    return c


def test(f):
    c = round(to_celsius(f), 2)
    print(f, "degrees fahrenheit is", c, "degrees celsius")


test(100)
test(88)
test(104)
test(112)
