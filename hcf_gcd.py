#Python program to find the HCF of GCD (user inputs)

from re import I


number1 = int(input("Enter first number here: "))
number2 = int(input("Enter second number here: "))

def compute_hcf(x, y):
    if (x > y):
        smaller = y
    else:
        smaller = x
    for i in range (1, smaller + 1):
        if ((x % i == 0) and (y % i == 0)):
            hcf = i 
    return hcf 

print ("The HCF is ", compute_hcf(number1, number2))