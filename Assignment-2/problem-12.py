# Write a program that calculates the factorial of a number.

number=int(input("Enter the number : "))
sum=1
if(number!=0):
    for i in range(1,number+1):
        sum=sum*i
    print(f"{number} is factorial = {sum}")
else:
    print(f"{number} is factorial = 0")