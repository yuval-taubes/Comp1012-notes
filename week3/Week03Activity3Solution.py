#COMP 1012 Week 3 Activity 3

#Note: isnumeric() checks if each character in a string is a digit
#      in the range 0 to 9, and returns True when that is the case.
#      A - sign or . decimal point will give False, so isnumeric()
#      is really testing for positive integers.

import math

userInput = input("Input s to Squared r for square Root, q to Quit: ")

while not userInput == 'q':
    if userInput == 's':
        #process square case
        num = input("Enter a positive integer to square: ")
        if num.isnumeric():
            num = int(num)
            print("{} squared is {}".format(num, num**2))
        else:
            print("That is not a positive number.")
    elif userInput == 'r':
        #process square root case
        num = input("Enter a positive integer to calculate the square root: ")
        if num.isnumeric():
            num = int(num)
            print("The square root of {} is {:.4f}".format(num, math.sqrt(num)))
        else:
            print("There is no square root of", num)
            
    #whether user entered 's', 'r', or invalid input, ask again
    userInput = input("Input s to Square, r for square Root, q to Quit: ")
