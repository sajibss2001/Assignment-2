# Write a program that finds the sum of all even numbers between 1 and `n`.

number=int(input("Enter the number : "))
sum=0
for i in range(1,number+1):
    if(i%2==0):
        sum=sum+i
print(f"Sum of all even number = {sum}")