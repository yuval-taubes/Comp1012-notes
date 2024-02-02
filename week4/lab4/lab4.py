# Reading Data From File
assignment_scores = []
test_scores = []
id_numbers = []

with open('week4\lab4\marks.csv', 'r') as file:
    file.readline()
    
    for line in file:
        id_number, assignment_score, test_score = map(float, line.strip().split(','))
        
        assignment_scores.append(assignment_score)
        test_scores.append(test_score)
        id_numbers.append(int(id_number))

print("Assignment Scores:", assignment_scores)
print("Test Scores:", test_scores)
print("User Id's", id_numbers)

average_assignment = sum(assignment_scores) / len(assignment_scores)
min_assignment = min(assignment_scores)
max_assignment = max(assignment_scores)

print("Assignment Scores Statistics:")
print("Average Score:", average_assignment)
print("Minimum Score:", min_assignment)
print("Maximum Score:", max_assignment)
