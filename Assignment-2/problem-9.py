# Write a program that determines if a number is positive, negative, or zero.

number=float(input("Enter the number : "))
if(number>0):
    print(f"{number} is positive number")
elif(number<0):
    print(f"{number} is negative number")
else:
    print(f"{number} is Zero")