# to calculate the area of a triangle by taking input from a user
import math

a = input ("Enter first side here: ")
b = input ("Enter second side here: ")
c = input ("Enter third side here: ")
is_valid = False 

try:
    a = (float(a))
    b = (float(b))
    c = (float(c))
    is_valid = True 

except:
    print ("Invalid input")

#to calculate semi-perimeter, find s

s = (a + b + c) / 2


#to calculate the area;
if is_valid == True:
    area = (s * (s-a) * (s-b) * (s-b)) ** 0.5
    print ("The area of the triangle is %0.2f" % area)
    print (area)

if is_valid == True:
    areas = math.sqrt((s * (s-a) * (s-b) * (s-b)))
    print ("Robert is as big as %0.3f" % areas)