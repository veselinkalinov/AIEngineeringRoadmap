import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]:
    print("hello, my name is", arg)


#  >> C:\Projects\Road to AI Engineer\stage-02-python-software-design\CS50P\Week 4 - Libraries\Lecture> python name.py Veselin

# >> hello, my name is Veselin
