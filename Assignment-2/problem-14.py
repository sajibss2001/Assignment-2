# Write a program that checks if a given number is prime or not.

number=int(input("Enter the number : "))
count=0 #divied checker
for i in range(2,number):
    if(number%i==0):
        count=count+1

if(number==0 or number==1):
    print(f"{number} is not prime number")
elif(count==0):
    print(f"{number} is prime number")
else:
    print(f"{number} is not prime number")