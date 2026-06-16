name = input("What is your name?: ")

# Ways to print - params and variables
# print(*objects, sep=' ', end='\n', file=sys.stdout, flush = False)

# end is '\n' by default, so we type end="" so the name prints on the same line
print("hello, ", end="")
print(name)

print("hello,", name, sep=" -> ")
print("hello, " + name)
print(f"hello, {name}")
