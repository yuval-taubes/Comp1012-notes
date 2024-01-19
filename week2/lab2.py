#area of a triangle

height = float(input("what is the height of the triangle: "))
width = float(input("what is the width of the triangle: "))


def calc_triange_area(height, width):
    return (height * width) / 2

triangle_area = calc_triange_area(height, width)

print("The area of the triangle is {}".format(triangle_area))

# convert miles to km

mile_distance = float(input("How many miles: "))

def convert_mile_to_km(mile):
    return mile * 1.61

km_distance = convert_mile_to_km(mile_distance)

print("The distnace in km is {:0.2f}".format(km_distance))


#Favorite Foods 

user_input_food_list = str(input("Enter a comma-seperated list of at least three of your favorite foods:"))
second_food = user_input_food_list.split(",")[1]

print("the second food is {}".format(second_food))


# escape sequecnes

print("She said \"Let’s go skiing. It’s snowing in July!\"")
print("The best set of numbers is {{1, 2, 3, 4}} {}".format("hello"))
print("Day\t Time Movie\nMonday 7:30 Shrek\nTuesday 9:00 Toy Story")
