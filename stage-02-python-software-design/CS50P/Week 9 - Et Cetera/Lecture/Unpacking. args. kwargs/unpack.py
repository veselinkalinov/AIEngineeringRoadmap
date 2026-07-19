def total(galleons: int, sickles: int, knuts: int) -> int:
    return (galleons * 17 + sickles) * 29 + knuts


# Unpacking

coins = [100, 50, 25]

print("--- Unpacking a list ---")
# '*'  infront of the list (data structure) "unpacks" it and passes it individually
print(total(*coins), "Knuts")  # "*coins" - unpacking
print("")

# Unpacking a dictionary

coins_dict = {
    "galleons": 100,
    "sickles": 50,
    "knuts": 25,
}

print("--- Unpacking a dictionary ---")
# '**' infront of the dictionary "unpacks" it and passes it individually
print(total(**coins_dict), "Knuts")  # "**coins_dict" - unpacking a dictionary
print("")
