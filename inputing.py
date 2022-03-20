from math import sqrt
name = input ("Enter number here: ")
is_valid = False

try: 
    name = float (name)
    is_valid =  True
except: 
    print ("Invalid input")

if (is_valid == True):
    nums = sqrt (name)
    print ("The user entered the number: " + str(name) + (". And the square root is: " + str(nums)))
