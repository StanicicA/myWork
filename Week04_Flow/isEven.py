#Ask the user to tyoe in a number
#program will then tell the user if the number is even or odd
#Author: Andrea Stanicic

number = int(input("enter an integer:"))
if (number % 2) == 0:
    print ("{} is an even number".format(number))
else:
    print("{} is an odd number".format(number))