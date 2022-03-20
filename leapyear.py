#python program to check if a year is a leap year by taking input from user

year = int(input("Enter the year to check if it was a leap year: "))

if (year % 400 == 0) and (year % 100 == 0):
    print (str(year) + " is a leap year")
elif (year % 4 == 0) and (year %100 != 0):
    print (str(year) + " is a leap year")
else:
    print (str(year) + " is not a leap year")