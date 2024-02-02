# Constants for calories per gram
APPLE_CALORIES = 52
CHICKEN_BREAST_CALORIES = 165
PASTA_CALORIES = 158
AVOCADO_CALORIES = 80
SPINACH_CALORIES = 11

# Constants for portion size in grams
APPLE_PORTION_SIZE = 100
CHICKEN_BREAST_PORTION_SIZE = 150
PASTA_PORTION_SIZE = 200
AVOCADO_PORTION_SIZE = 50
SPINACH_PORTION_SIZE = 50

# Constants for calories per portion size
APPLE_CALORIES_PER_GRAM = APPLE_CALORIES / APPLE_PORTION_SIZE
CHICKEN_BREAST_CALORIES_PER_GRAM = CHICKEN_BREAST_CALORIES / CHICKEN_BREAST_PORTION_SIZE
PASTA_CALORIES_PER_GRAM = PASTA_CALORIES / PASTA_PORTION_SIZE
AVOCADO_CALORIES_PER_GRAM = AVOCADO_CALORIES / AVOCADO_PORTION_SIZE
SPINACH_CALORIES_PER_GRAM = SPINACH_CALORIES / SPINACH_PORTION_SIZE

run_menu = True

calories_consumed = 0

while(run_menu):
    run_food_input_menu = True

    weight = float(input("Please enter your weight (kg): "))
    height = float(input("please enter you height (meters): "))

    bmi = weight / (height *  height)
    bmi_category = None
    recomended_calories = None

    #bmi calculation and output
    if bmi < 18.5:
        bmi_category = "Underweight"
        recomended_calories = 2200
    elif bmi >= 18.5 and bmi <= 24.9:
        bmi_category = "Normal weight"
        recomended_calories = 2000
    elif bmi >= 25 and bmi <= 29.9:
        bmi_category = "overweight"
        recomended_calories = 1800
    else:
        bmi_category= "obese"
        recomended_calories = 1500

    print("Your BMI is {}, which falls into the {} weight category".format(bmi, bmi_category))
    print("your recomendded calories is {}".format(recomended_calories))

    while(run_food_input_menu):
        print("diet planning")
        print("Choose form the following foods (enter 0 when done) \n1. Apple \n2. Chicken Breast \n3. Pasta \n4. Avocado \n5. Spinach")
        food_selection_input = int(input("enter your selection: "))
        food_selection = None
        if(food_selection_input == 1):
            food_selection = APPLE_CALORIES_PER_GRAM

        elif(food_selection_input == 2):
            food_selection = CHICKEN_BREAST_CALORIES_PER_GRAM

        elif(food_selection_input == 3):
            food_selection = PASTA_CALORIES_PER_GRAM

        elif(food_selection_input == 4):
            food_selection = AVOCADO_CALORIES_PER_GRAM

        elif(food_selection_input == 5):
            food_selection = SPINACH_CALORIES_PER_GRAM

        else:
            break

        grams = float(input("Enter the portion size (in grams): "))

        calories = grams * food_selection
        calories_consumed += calories
        print("This meal contained {:.2f} calories".format(calories))


    print("you have consumed {} calories".format(calories_consumed))
    if(calories_consumed > recomended_calories):
        print("you have exceded your recomended calories")
    elif(calories_consumed < recomended_calories):
        print("you have consumed fewer calories than recomended")
    else:
        print("You have consumed the recomended amount of calories")
