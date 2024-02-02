#COMP 1012 Week 3 Activity 2

sum = 0

text = input("Enter a number or q to quit: ")

while text != "q":
    if text.isnumeric():
        userNum = int(text)
        sum = sum + userNum
        text = input("Enter another number or q to quit: ")
    else:
        text = input("That's not a number! Try again: ")
        
print("The total of all numbers is " + str(sum))