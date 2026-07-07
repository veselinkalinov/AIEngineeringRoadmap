'''
Assignment

We need to calculate the size of a weapon's "attack area." With a 1.0 meter sword, for example, a player can attack in an area of 3.14 square meters around them. You can use the area_of_circle function to do that calculation.

Fix the bug where spear_area is 0 by calling the area_of_circle function with the spear_length as input and store the result in the spear_area variable.
'''


def area_of_circle(radius):
    pi = 3.14
    area = pi * pow(radius, 2)
    return area


sword_length = 1.0
spear_length = 2.0


sword_area = area_of_circle(sword_length)
spear_area = area_of_circle(spear_length)


print("Sword length:", sword_length, "meters.")
print("Sword attack area:", sword_area, "square meters")

print("Spear length:", spear_length, "meters.")
print("Spear attack area:", spear_area, "square meters")
