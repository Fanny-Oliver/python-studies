#Python program to find the LCM of 3 numbers (user inputs)

from re import X


num1 = int(input("Enter first number here: "))
num2 = int(input("Enter second number here: "))
num3 = int(input("Enter third number here: "))

def compute_lcm (x, y, z):
    if (x > y) and (x > z):
        greater = x 
    elif (y > x) and (y > z):
        greater = y
    else:
        greater = z
    while (True):
        if ((greater % x == 0) and (greater % y == 0) and (greater % z == 0)):
            lcm = greater 
            break
        greater += 1
    return lcm
"""
i = 1
while (True):
    print (i)
    i += 1
"""
print ("The LCM is equal to: ", compute_lcm(num1,num2,num3) )
