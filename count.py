text = input("Enter string: ")
digits = 0
letters = 0
for i in text:
    if (i >= 'a' and i <= 'z') or (i >= 'A' and i <= 'Z'):
        letters += 1
    elif (i >= '0' and i <= '9'):
        digits += 1
print("Letters:", letters)
print("Digits:", digits)
