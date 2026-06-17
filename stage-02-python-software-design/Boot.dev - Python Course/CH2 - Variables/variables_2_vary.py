'''
We need to reduce our hero's health as they take damage.

Before each print() function in the provided code, change the value of player_health to 100 less than it was before.
'''


def health_loss(ph: int) -> int:
    ph -= 100
    return ph


player_health = 1000

player_health = health_loss(player_health)

print(player_health)

player_health = health_loss(player_health)

print(player_health)

player_health = health_loss(player_health)

print(player_health)

player_health = health_loss(player_health)

print(player_health)
