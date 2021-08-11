import re

text = input("Enter comma seperated passwords:")
passwords = re.split(", |,", text)
for password in passwords:
    small = 0
    capital = 0
    digit = 0
    character = 0
    if len(password) >= 6 and len(password) <= 12:
        for char in password:
            if (char >= 'a' and char <= 'z'):
                small += 1
            if (char >= 'A' and char <= 'Z'):
                capital += 1
            if (char >= '0' and char <= '9'):
                digit += 1
            if (char >= 'a' and char <= 'z'):
                small += 1
            if (char == '$' or char == '#' or char == '@'):
                character += 1
    if (small >= 1 and capital >= 1 and digit >= 1 and character >= 1):
        print(password, end=",")
