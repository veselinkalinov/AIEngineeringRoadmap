# Creating my own libraries example (+ say.py)

def main():
    hello("world")
    goodbye("world")


def hello(name):
    print(f"hello, {name}")


def goodbye(name):
    print(f"goodbye, {name}")


'''
When we import a function from that file in another file "import sayings" makes python to read the whole sayings.py including the main() at the bottom which makes him execute it even tho we dont want to. To prevent that in python we have to use:
'''
if __name__ == "__main__":
    main()
