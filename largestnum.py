#Python program to find the largest number among 3 numbers enters by a user

num1 = float(input("Enter first number here: "))
num2 = float(input("Enter second number here: "))
num3 = float(input("Enter third number here: "))

if (num1 > num2) and (num1 > num3):
    largest = num1
elif (num2 > num1) and (num2 > num3):
    largest = num2
else:
    largest = 3

print ("The largest number is " + str(largest))
