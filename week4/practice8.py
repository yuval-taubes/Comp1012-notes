data = [8, 19, 24, 37, 39, 41, 49, 53, 58, 25, 81, 90]
highest_data = 0
is_accesnding = True
for i in range(len(data)):
    if highest_data > data[i]:
        is_accesnding = False


print("is the list in assending order? (true or false) {}".format(is_accesnding))