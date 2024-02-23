#1.1
def are_anagrams(word1, word2):
    set1 = set(word1)
    set2 = set(word2)
    
    return set1 == set2

word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")

if are_anagrams(word1, word2):
    print(f"{word1} and {word2} are anagrams.")
else:
    print(f"{word1} and {word2} are not anagrams.")

#1.2
    
def are_anagrams_with_duplicates(word1, word2):
    dict1 = {}
    dict2 = {}

    for char in word1:
        # dict1[char] = dict1.get(char) + 1
        if char not in dict1:
            dict1[char] = 0
        dict1[char] += 1

    for char in word2:
        dict2[char] = dict2.get(char) + 1

    return dict1 == dict2

# Get input from the user
word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")

# Check if the words are anagrams with duplicates
if are_anagrams_with_duplicates(word1, word2):
    print(f"{word1} and {word2} are anagrams with duplicates.")
else:
    print(f"{word1} and {word2} are not anagrams with duplicates.")

#2
days = {1: "Sunday", 2: "Monday", 3: "Tuesday", 4: "Wednesday", 5: "Thursday", 6: "Friday", 7: "Saturday"}
months = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}

day = int(input("Enter the day (1-31): "))
month = int(input("Enter the month (1-12): "))
year = int(input("Enter the year: "))
day_of_week = int(input("Enter the day of the week (1-7): "))

print(f"{days[day_of_week]}, {months[month]} {day}, {year}")
