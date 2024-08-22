# Write a program that swaps the values of two variables.

num_1=input("Enter the 1st number : ")
num_2=input("Enter the 2nd number : ")
print("Before Swaping : ")
print(f"num_1 : {num_1}\nnum_2 : {num_2}")

num_1,num_2=num_2,num_1
print("After Sawping : ")
print(f"num_1 : {num_1}\nnum_2 : {num_2}")