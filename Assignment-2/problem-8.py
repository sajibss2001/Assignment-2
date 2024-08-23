# Write a program that determines if a year is a leap year or not.

year=int(input("Enter the Year : "))
if((year%4==0 and year%100!=0) or year%400==0):
    print(f"{year} is Leap year")
else:
    print(f"{year} is not Leap year")
