name = input("What is your name?: ")

# Remove whitespace from str: input: "space space" Vesko "space space" -> output: Vesko
name = name.strip()

# Capitalizes "ONLY THE FIRST" element of a string: input: veselin kalinov -> output: Veselin kalinov
name = name.capitalize()

# Capitalizes the first letter of every string separated by a space: input: veselin kalinov -> output: Veselin Kalinov
name = name.title()

# Chaining functions
name = name.strip().title()
name = input("What is your name?: ").strip().title()

# Split users name into first and last name
# -> from left to right of a string: input: veselin kalinov -> first: veselin, last: kalinov
first, last = name.split(" ")

# Ways to print - params and variables
# print(*objects, sep=' ', end='\n', file=sys.stdout, flush = False)

# end is '\n' by default, so we type end="" so the name prints on the same line
print("hello, ", end="")
print(first)

print("hello,", name, sep=" -> ")
print("hello, " + name)
print(f"hello, {name}")
