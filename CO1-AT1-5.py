import re

emails = [
    "john@gmail.com",
    "student@college.edu",
    "abc@yahoo.org",
    "user123@test.in",
    "wrong_email@com"
]

pattern = re.compile(
    r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.(com|org|edu|in)$'
)

for email in emails:
    if pattern.fullmatch(email):
        print(email, "-> Valid")
    else:
        print(email, "-> Invalid")
