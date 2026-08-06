# Program to demonstrate Regular Expressions in Python

import re

text = "My phone number is 9876543210 and email is student123@gmail.com"

# Search for a phone number
phone = re.search(r"\d{10}", text)

if phone:
    print("Phone Number:", phone.group())

# Search for an email
email = re.search(r"\S+@\S+", text)

if email:
    print("Email:", email.group())

# Find all words starting with 's'
words = re.findall(r"\bs\w*", text, re.IGNORECASE)

print("Words starting with 's':", words)
