#username = input ("Enter user name: ")
#print ("The Username is " + username)

from math import sqrt 
numbera = input ("Enter number here: ")
is_valid = False

try:
    numbera = float (numbera)
    is_valid = True
except:
    print ("Invalid Number")
    


#if (type(numbera) != int and type(numbera) != float):
 #   print ("Invalid input, must be an integer or a float")
if (is_valid == True):
    nume = sqrt (numbera)
    print ("The square root of " + str(numbera) + " is " + str(nume))

if (is_valid == True):
    nums= numbera ** 3
    print ("The cube root of " + str(numbera) + " is " + str(nums))

