height = int(input("please enter a height: "))
iteration = 0

while iteration <= height:
    print("*" * iteration)
    iteration+= 1


# Ask the user to input the height of the triangle
height = int(input("Please enter the height of the triangle: "))

# Loop to print each line of the triangle
for i in range(1, height + 1):
    print('*' * i)
