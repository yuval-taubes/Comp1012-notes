#COMP 1012 Week 4 Activity 2

FILENAME = "week4Test.txt"
VOWELS = "aeiou"

theFile = open(FILENAME)

numChars = 0
numWords = 0
numVowels = 0
lineCounter = 0

for line in theFile:  #for each line in the file
    currChars = len(line) #number of characters in the current line
    
    wordList = line.split()
    currWords = len(wordList) #number or words in the current line
    
    currVowels = 0
    for char in line:  #for each character in the current line
        if char in VOWELS:  #if the character is one of the characters in the VOWELS string
            currVowels += 1
            
    output = "Line {} has {} characters, including {} vowels, and {} words."
    print(output.format(lineCounter, currChars, currVowels, currWords))
    
    #add counts for current line to the file totals
    numChars += currChars
    numWords += currWords
    numVowels += currVowels
    lineCounter += 1

theFile.close()

output = "\nThe file has {} lines, {} characters including {} vowels, and {} words."
print(output.format(lineCounter, numChars, numVowels, numWords))
    

#file statistics
avgCharPerLine = numChars/lineCounter
avgCharPerWord = numChars/numWords  #ignores spaces
percentVowels = 100*numVowels/numChars

print("\nThe average characters per line was {:.2f}.".format(avgCharPerLine))
print("The average characters per word was {:.2f}.".format(avgCharPerWord))
print("The percentage of characters that were vowels was {:.2f}%.\n".format(percentVowels))

print("End of processing")
    
    
    