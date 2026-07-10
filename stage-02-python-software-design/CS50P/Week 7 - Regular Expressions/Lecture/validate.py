import re

email = input("What's your email? ").strip()

# re.search(pattern, string, flags=0(re.IGNORECASE, re.MULTILINE, re.DOTALL)))
# 1. r"..." → raw string, useful for regex in Python
# 2. ^ → start of the string
# 3. [\w.-]+ → one or more “word” characters: letters, numbers, or _,.,-
# 4. @ → must contain an @
# 5. [\w.-]+ → domain name with only letters, numbers, or _,.,-
# 6. \. → a real dot .
# 7. edu → must end with edu
# 8. $ → end of the string

if re.search(r"^[\w.-]+@[\w.-]+\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")
