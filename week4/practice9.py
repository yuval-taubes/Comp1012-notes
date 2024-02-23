listOne = [8, 19, 53, 27, 31, 82, 16, 72, 3, 22]
listTwo = [82, 74, 20, 31, 19, 22, 65, 27, 45]

count = 0

for item in listOne:
    for item2 in listTwo:
        if item == item2:
            count+= 1

print(count)