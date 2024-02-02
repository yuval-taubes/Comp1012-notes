# message = "The quick brown fox jumped over the lazy dog"
# wordToFind = "lazy"
# wordIndex = message.find(wordToFind)
# extractedWord = message[wordIndex: (wordIndex + len(wordToFind))]
# print(wordIndex)
# print(extractedWord)

# lyrics = "Baby baby ohhhh"
# firstSpace = lyrics.rfind(" ")

# print(firstSpace)
# extractedWord = lyrics[0: firstSpace]

# print(extractedWord)

# x = 20 > 100
# x = not x
# print(x)

# a = False
# b = True
# c = True
# d = False
# x = (a or b) and not (c or d)
# print(x)

# x = 10
# y = 0
# while x > 5:
#     y = y + 1
#     x = x - 2
# print("x: {}, y: {}".format(x,y))

assignment_scores = []
test_scores = []

file_path = 'marks.csv'

file_exists = open(file_path, 'r').readline() != ""

if not file_exists:
    print(f"Error: File '{file_path}' not found.")
else:
   
    file = open(file_path, 'r')

   
    header_line = file.readline()

    lines = [header_line] + file.readlines()


    for line in lines:
        columns = line.strip().split(',')
        if len(columns) >= 3:
            assignment_scores.append(float(columns[1]))
            test_scores.append(float(columns[2]))

    file.close()

   
    if len(assignment_scores) > 0:
       
        print("Assignment Scores:", assignment_scores)
        print("Test Scores:", test_scores)

        average_assignment = sum(assignment_scores) / len(assignment_scores)
        minimum_assignment = min(assignment_scores)
        maximum_assignment = max(assignment_scores)

        print("\nAverage Assignment Score:", average_assignment)
        print("Minimum Assignment Score:", minimum_assignment)
        print("Maximum Assignment Score:", maximum_assignment)
    else:
        print("No assignment scores found in the file.")