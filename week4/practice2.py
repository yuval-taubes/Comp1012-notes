run_menu = True

saying = input("Please enter your favourite saying: ")

letter = input("Please enter a letter to look for: ")

count = 0

for char in saying:
    if char == letter:
        count += 1
        print(char)

print("There were {} instances of the letter {} in the phrase {}".format(count, letter, saying))
