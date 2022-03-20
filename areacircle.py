#calculating the area of a circle byt taking input from user

PI = 3.14
r = input ("Input the value of r here: ")
is_valid = False 

try:
    r = float (r)
    is_valid = True 

except: 
    print ("Invalid input")


if is_valid == True:
    area = PI * r * r
    print ("The area of the circle is: " + str (area))
