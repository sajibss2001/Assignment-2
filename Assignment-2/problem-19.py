# Write a program that generates a random number and allows the user to guess it.

import random
number=int(input("Enter number range 0 to 10 : "))
number1=int(random.uniform(0,10))
print(f"Random number : {number1}")
if(number==number1):
    print("You are right")
else:
    print("You are wrong")
