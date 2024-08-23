# Write a program that finds the greatest common divisor (GCD) of two numbers.

num_1=int(input("Enter the first number : "))
num_2=int(input("Enter the second number : "))
GCD=0
i=1
while(i<=num_1 and i<=num_2):
    if(num_1%i==0 and num_2%i==0):
        GCD=i
    i=i+1

print(f"GCD = {GCD}")
