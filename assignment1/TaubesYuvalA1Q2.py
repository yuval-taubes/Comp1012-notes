odd_number_count = 0
even_number_count = 0
positive_number_count = 0
negative_number_count = 0
single_digit_magnitude_count = 0
two_digit_magnitude_count = 0
three_digit_magnitude_count = 0

loop_menu = True

while(loop_menu):
    user_input = (input("enter a number (done to exit)"))
    number = None
    if(user_input.lower() == "done"):
        loop_menu = False
        break
    else:
        number = int(user_input)
    

    if number % 2 == 0:
        print("The number is even.")
        even_number_count += 1
    else:
        print("The number is odd.")
        odd_number_count += 1

    if number > 0:
        print("The number is positive.")
        positive_number_count += 1
    elif number < 0:
        print("The number is negative.")
        negative_number_count += 1
    else:
        print("The number is zero.")


    absolute_value = abs(number)
    
    if 0 <= absolute_value <= 9:
        print("The number has: One Digit")
        single_digit_magnitude_count += 1
    elif 10 <= absolute_value <= 99:
        print("The number has: Two Digits")
        two_digit_magnitude_count += 1
    else:
        print("The number has: Three or More Digits")
        three_digit_magnitude_count += 1


print("-----------------------summary----------------------")
print("odd numbers {}".format(odd_number_count))
print("even number {}".format(even_number_count))
print("positve number {}".format(positive_number_count))
print("negative number {}".format(negative_number_count))
print("single digit number {}".format(single_digit_magnitude_count))
print("two digit number {}".format(two_digit_magnitude_count))
print("three digit number {}".format(three_digit_magnitude_count))




