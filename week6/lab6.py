#1
days = {1: "Sunday", 2: "Monday", 3: "Tuesday", 4: "Wednesday", 5: "Thursday", 6: "Friday", 7: "Saturday"}
months = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}

def get_valid_month():
    run_loop = True
    while run_loop:
        month = int(input("Enter the month (1-12): "))
        if 1 <= month <= 12:
            return month
        else:
            print("Invalid month. Please enter a number between 1 and 12.")

def get_valid_day(month):
    run_loop = True
    while run_loop:
        day = int(input("Enter the day (1-31): "))
        if 1 <= day <= 31:
            if month == 2 and day > 28:
                print("Invalid day for February. Please enter a number between 1 and 28.")
            elif month in [4, 6, 9, 11] and day > 30:
                print("Invalid day for {}. Please enter a number between 1 and 30.".format(months[month]))
            else:
                return day
        else:
            print("Invalid day. Please enter a number between 1 and 31.")

def get_valid_year():
    run_loop = True
    while run_loop:
        year = int(input("Enter the year: "))
        if 1900 <= year <= 2100:
            return year
        else:
            print("Invalid year. Please enter a 4-digit number between 1900 and 2100.")

def get_valid_day_of_week():
    run_loop = True
    while run_loop:
        day_of_week = int(input("Enter the day of the week (1-7): "))
        if 1 <= day_of_week <= 7:
            return day_of_week
        else:
            print("Invalid day of the week. Please enter a number between 1 and 7.")

month = get_valid_month()
day = get_valid_day(month)
year = get_valid_year()
day_of_week = get_valid_day_of_week()

print(f"{days[day_of_week]}, {months[month]} {day}, {year}")


#2
def sumList(theList):
    total = 0
    for number in theList:
        total += number
    return total

def max(firstNum, secondNum):
    if firstNum > secondNum:
        return firstNum
    else:
        return secondNum

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a = 0 
        b = 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

numbers = [1, 2, 3, 4, 5]
print(sumList(numbers))

num1 = 10
num2 = 20
print(max(num1, num2))

n = 5
print(f"Fibonacci({n}): {fibonacci(n)}")
