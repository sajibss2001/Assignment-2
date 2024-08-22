# Write a program that converts temperature from Fahrenheit to Celsius.

farenhit_temp=float(input("Enter the farenhit tempature : "))
celcius_temp=round((5*(farenhit_temp-32))/9,2)
print(f"Celsius Tempareture : {celcius_temp}")