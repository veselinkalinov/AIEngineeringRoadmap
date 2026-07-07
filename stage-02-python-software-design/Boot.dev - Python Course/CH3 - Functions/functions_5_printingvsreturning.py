'''
print() is a function that:

    Prints a value to the console
    Does not return a value

return is a keyword that:

    Ends the current function's execution
    Provides a value (or values) back to the caller of the function
    Does not print anything to the console (unless the return value is later print()ed)


Assignment

There's a problem in the get_title function! It's supposed to construct the title value and return it to the caller. Instead, it's barbarically printing the value to the console.

Fix the get_title function.

    Return the title
    Do not print it inside get_title
'''


def get_title(first_name: str, last_name: str, job: str) -> str:
    title = first_name + " " + last_name + " the " + job
    return title


def test(first_name, last_name, job):
    title = get_title(first_name, last_name, job)
    print("First name:", first_name)
    print("Last name:", last_name)
    print("Job:", job)
    print("Title:", title)
    print("=====================================")


test("Frodo", "Baggins", "warrior")
test("Bilbo", "Baggins", "thief")
test("Gandalf", "The Grey", "wizard")
test("Aragorn", "Son of Arathorn", "ranger")
