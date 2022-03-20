#Python program to find the factors of a number

from operator import is_


number = input("Enter number here: ")
is_valid = False
factor = []
#def print_factors(number):
try:
    number = int(number)
    is_valid = True
except:
    print ("Invalid figure")

print ("The factors of " + str(number) + " are: ")
for i in range(1, number + 1):
    if (number % i == 0):
        #print (i)
        factor.append(i)
#number = 340

print(factor)