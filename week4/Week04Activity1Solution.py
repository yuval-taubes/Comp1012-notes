# COMP 1012 Week 4 Activity 1
# Sum the even numbers in the list

data = [32, 65, 82, 24, 19, 30, 86, 34, 57, 91, 60]

'''
#Challenge
data = []
userInput = "go"  #to avoid duplicating the line asking for input, use any string that is not 'quit'
while userInput != 'q':
    userInput = input("Please enter a positive integer, or q to quit: ")
    if userInput.isnumeric():
        data.append( int(userInput) )
    else:
        print("That's not a positive integer!")

print("The positive integers entered were:", data)
'''


theSum = 0

for num in data:  #for each number in the list
    if (num % 2 == 0):  #if the remainder is zero when dividing by 2, the number is even
        theSum += num
        
print("The sum of the even numbers was " + str(theSum))
        