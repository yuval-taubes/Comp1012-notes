
myFile = open("test.txt")

theDict = dict()  #will be length:count pairs for key:value (e.g. 3:20 means there are twenty words with three letters)

for line in myFile:  #for every line in the file
    words = line.split()  #split on whitespace
    for word in words:  #for every word in the line
        length = len(word)
        if length not in theDict: #if we have not seen this length before
            theDict[length] = 0  #add it to the dictionary
        theDict[length] += 1 #increase the count associated with the length
        
print(theDict)

for key in theDict:
    print("There are {} words that have a length of {}".format( theDict[key], key ))
