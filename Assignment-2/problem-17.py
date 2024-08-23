# Write a program that reverses a given number.

number=str(input("Enter the number : "))
print(f"Your number : {number}")
print(f"Riverse number : ",end="")
for i in range(len(number)-1,-1,-1):
    print(number[i],end="")
