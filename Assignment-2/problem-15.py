# Write a program that prints the multiplication table of a given number.

number=int(input("Enter the number : "))
print(f"Multiplication table\n")
for i in range(1,11):
    print(f"{number} * {i} = {number*i}")