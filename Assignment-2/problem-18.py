# Write a program that checks if a given string, is a palindrome.

value=str(input("Enter the string : "))
value1=value[::-1] #string reverse
if(value==value1):
    print("Given string is palindrome")
else:
    print("Given string is not palindrome")
