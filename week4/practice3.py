# Get the user's favourite saying as input
saying = input("Please enter your favourite saying: ")

# Create a dictionary to store the count of each letter
letter_count = {}

# Iterate through each character in the saying
for char in saying:
    # Check if the character is a letter (ignoring spaces)
    if char.isalpha():
        # Convert the character to lowercase to ignore capitalization
        char_lower = char.lower()
        # Update the count for the current letter in the dictionary
        letter_count[char_lower] = letter_count.get(char_lower, 0) + 1

# Find the letter with the highest count
most_frequent_letter = max(letter_count, key=letter_count.get)

# Print the result
print(f"The most frequent letter (ignoring capitalization) is '{most_frequent_letter}' with a count of {letter_count[most_frequent_letter]}.")
