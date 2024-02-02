#COMP 1012 Week 3 Activity 1

LETTER = 'm'

text = input("Please enter a 5-letter word: ")
while len(text) != 5 or not text.isalpha() or text.find(LETTER) == -1:
    text = input("Invalid input.  Please try again: ")
    
print("Input valid.  You entered: " + text + ".")