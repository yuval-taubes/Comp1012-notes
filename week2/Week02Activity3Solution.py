#COMP 1012 Week 2 Activity 3: Lyrics

#get lyrics from user
lyrics = input("Please enter your favourite lyrics: ")

#extract first word
firstSpace = lyrics.find(" ")
firstWord = lyrics[:firstSpace] #up to but not including the first space
print("First word: " + firstWord)

#extract the last word
lastSpace = lyrics.rfind(" ")
lastWord = lyrics[lastSpace+1:] #+1 to omit the space
print("Last word: " + lastWord)

#extract the third word
secondSpace = lyrics.find(" ",firstSpace+1) #+1 to avoid finding the same space
thirdSpace = lyrics.find(" ",secondSpace+1)
thirdWord = lyrics[secondSpace+1:thirdSpace] #+1 to omit the space
print("Third word: " + thirdWord)

#get a letter from user
letter = input("Please enter a letter: ")

#find second occurrence of the letter
firstLetter = lyrics.find(letter)
secondLetter = lyrics.find(letter, firstLetter+1) #+1 to avoid finding same occurrence

#find space before second letter
beforeLetter = lyrics.rfind(" ", 0, secondLetter) #find last space before letter

#find space after second letter
afterLetter = lyrics.find(" ", secondLetter)

#extract word with letter
letterWord = lyrics[beforeLetter+1:afterLetter]
print("Second word containing " + letter + ": " + letterWord)
