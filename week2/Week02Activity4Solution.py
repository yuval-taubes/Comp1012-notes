#COMP 1012 Week 2 Activity 4: Mortgage Payments

#get information from user
principal = float(input("Please enter the principal, in dollars: "))
yearlyRate = float(input("Please enter the yearly interest rate (e.g. 3 for 3%): "))
years = float(input("Please enter the number of years to pay off the loan: "))

#intermediate calculations
monthlyRate = (yearlyRate/12)/100  #as a decimal, e.g. 0.03 for 3%
months = int(years*12)  #integer number of payments

#find amount of monthly payment
power = pow(1+monthlyRate , months)
payment = principal * (monthlyRate * power) / (power - 1)

#print results
output = "For a principal of ${:.2f}, a yearly interest rate of {:.2f}%, "
output += "and a payback time of {:d} months, your monthly payment will be "
output += "${:.2f}"

formattedOutput = output.format(principal, yearlyRate, months, payment)

print(formattedOutput)