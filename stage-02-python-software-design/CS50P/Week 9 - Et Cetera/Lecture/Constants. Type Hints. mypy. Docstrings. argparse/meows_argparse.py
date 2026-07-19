import argparse

# import sys

# sys library

"""
if len(sys.argv) == 1:
    print("meow")
elif len(sys.argv) == 3 and sys.argv[1] == "-n":
    n = int(sys.argv[2])
    for _ in range(n):
        print("meow")
else:
    print("usage: meows_argparse.py.py")

"""

# argparse library

parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument(
    "-n", default=1, help="number of times to meow", type=int
)  # it gives a "python meows_argparse.py --help" message, default and a type of 'n'
args = parser.parse_args()

for _ in range(int(args.n)):
    print("meow")
