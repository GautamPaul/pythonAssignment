import re
import math
numbersString = input("Enter comma seperated numbers: ")
numbers = re.split(", |,", numbersString)
C = 50
H = 30
for D in numbers:
    print(round(math.sqrt((2*C*int(D))/H)), end=",")
