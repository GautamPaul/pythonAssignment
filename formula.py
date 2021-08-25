import re
import math
number_string = input("Enter comma seperated numbers: ")
numbers = re.split(", |,", number_string)
C = 50
H = 30
for D in numbers:
    print(round(math.sqrt((2*C*int(D))/H)), end=",")
