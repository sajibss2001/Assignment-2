# Write a program that generates a Fibonacci sequence of length `n`.

number=int(input("Enter the number : "))
num1=0
num2=1
print("0 1 ",end="")
for i in range(1,number+1):
    sum=num1+num2
    print(f"{sum} ",end="")
    num1=num2
    num2=sum
