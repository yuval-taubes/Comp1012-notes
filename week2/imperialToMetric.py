feet = float(input("How many Feet?: "))
inches = float(input("How many Inches?: "))

cm = (feet * 30.48) + (inches * 2.54)

print("{} feet {} inches is {:.1f} cm".format(feet, inches, cm))
