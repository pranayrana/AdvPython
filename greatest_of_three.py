#greatest_of_three.py

#ctonrol structures in python
#Conditional statements
#Find greatest of three numbers taking input from user
num1 = int(input("Enter first number: "))   
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 >= num2 and num1 >= num3:
    #print the greatest number
    print(f"The greatest number is: {num1}")
elif num2 >= num1 and num2 >= num3:
    #print the greatest number
    print(f"The greatest number is: {num2}")
else:
    #print the greatest number
    print(f"The greatest number is: {num3}")
