import re

email = "john.doe123@gmail.com"
password = "P@ssw0rd123"

email_pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.(com|org|edu|in)$'
password_pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%&!*])\S{8,}$'

if re.fullmatch(email_pattern, email):
    print("Valid Email")
else:
    print("Invalid Email")

if re.fullmatch(password_pattern, password):
    print("Strong Password")
else:
    print("Weak Password")
