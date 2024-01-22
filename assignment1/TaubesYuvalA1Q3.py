APPLE_CALORIES_PER_GRAM = 52 / 100
CHICKEN_BREAST_CALORIES_PER_GRAM = 165 / 150
PASTA_CALORIES_PER_GRAM = 158 / 200
AVOCADO_CALORIES_PER_GRAM = 80 / 50
SPINACH_CALORIES_PER_GRAM = 11 / 50

run_menu = True

calories_consumed = 0

while(run_menu):
    run_food_input_menu = True

    weight = float(input("Please enter your weight (kg): "))
    height = float(input("please enter you height (meters): "))

    bmi = weight / (height *  height)
    bmi_category = None
    recomended_calories = None

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
        print("Choose form the following foods (enter 0 when done) \n1.Apple \n2. Chicken Breast \n3. Pasta \n4. Avocado \n5. Spinach")
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
