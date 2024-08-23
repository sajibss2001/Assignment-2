# Write a program that calculates the grade based on a given percentage.

mark=float(input("Enter your mark : "))
if(mark>=80 and 100>=mark):
    print(f"Your grade point 'A+'")
elif(mark>=70 and mark<80):
    print("Your grade point is 'A'")
elif(mark>=60 and mark<70):
    print("Your grade point is 'A-'")
elif(mark>=50 and mark<60):
    print("Your grade point is 'B'")
elif(mark>=40 and mark<50):
    print("Your grade point is 'C'")
elif(mark>=33 and mark<40):
    print("Your is grade point is 'D'")
elif(mark>=0 and mark<33):
    print("Fail !!!")
else:
    print("Invalid number !!!!")