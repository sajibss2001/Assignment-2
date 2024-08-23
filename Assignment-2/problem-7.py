# Write a program that finds the maximum of three numbers.

num_1=float(input("Enter the 1st number : "))
num_2=float(input("Enter the 2nd number : "))
num_3=float(input("Enter the 3rd number : "))

if(num_1>num_2 and num_1>num_3):
    print(f"{num_1} is maximum number")
elif(num_2>num_3 and num_1>num_1):
    print(f"{num_2} is maximum number")
elif(num_3>num_1 and num_3>num_2):
    print(f"{num_3} is maximum number")
else:
    print("All number are equal")