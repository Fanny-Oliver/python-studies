"""
#First task 
#Find the Square Root from a random number generated between 2 and 200
from math import sqrt
import random
my_num = random.randrange(2, 200)

my_sqrt = sqrt (my_num)
print (str(my_sqrt) + " is the square root of " + str(my_num))

#i need help with task 2, so moving to number 3
"""

#finding the cube root

import random
#from math import sqrt
numbers = random.randrange (2, 200)
def cube_root (x):
    if (x < 0):
        x = abs(x)
        cube = x ** (1/3) * (-1)
    else:
        cube = x ** (1/3)
    return cube

#print (str(cube) + " is the cube root of " + str(numbers))
print (numbers)
print (cube_root(x=numbers))


