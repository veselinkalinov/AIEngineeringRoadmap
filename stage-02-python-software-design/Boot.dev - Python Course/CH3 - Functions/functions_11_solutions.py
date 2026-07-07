'''
Assignment

Enough about solution mechanics, let's write more code.

We need to display the current time to our players. The problem is that the time is stored as a number of hours, but we want to display it as a number of seconds. There are 60 seconds in a minute, but how many are in an hour?

Complete the hours_to_seconds function. It should convert hours to seconds and return the result.
'''


def hours_to_seconds(hours):
    s = hours * pow(60, 2)
    return s


def test(hours):
    secs = hours_to_seconds(hours)
    print(hours, "hours is", secs, "seconds")


test(10)
test(1)
test(25)
test(100)
test(33)
