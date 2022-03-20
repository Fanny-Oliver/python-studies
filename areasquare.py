#Python Program to Calculate the Area of a square 
# by taking the inputs required from a user

side = input ("Enter side here: ")
is_valid = False

try:
    side = float (side)
    is_valid = True 

except: 
    print ("Invalid number")

#to find the area of a square:

if is_valid == True:
    area = side * side 
    print ("The area os a square is: " + str (side) + " * " + str (side) + " = " + str(area))