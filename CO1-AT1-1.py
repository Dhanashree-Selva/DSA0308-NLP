import re

# Student Details
email = "john.doe123@gmail.com"
mobile = "+91-9876543210"
password = "P@ssw0rd123"
dob = "15/08/2004"
regno = "23AIML1056"

# Regex Patterns
email_pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
mobile_pattern = r'^\+91-\d{10}$'
password_pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%&!*])[A-Za-z\d@#$%&!*]{8,}$'
dob_pattern = r'^\d{2}/\d{2}/\d{4}$'
reg_pattern = r'^\d{2}[A-Z]{4}\d{4}$'

print("Email:", bool(re.fullmatch(email_pattern, email)))
print("Mobile:", bool(re.fullmatch(mobile_pattern, mobile)))
print("Password:", bool(re.fullmatch(password_pattern, password)))
print("DOB:", bool(re.fullmatch(dob_pattern, dob)))
print("Register Number:", bool(re.fullmatch(reg_pattern, regno)))
