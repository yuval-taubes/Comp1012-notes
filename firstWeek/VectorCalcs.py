import math
x1 = 5
y1 = 8
x2 = 10
y2 = -25
walkingSpeed = 4

xDiff = x2-x1
yDiff = y2-y1

distance = math.sqrt((xDiff)**2 + (yDiff)**2)

print(distance)

time = distance/walkingSpeed

formatedTime = "{:5.2f}".format(time)

print("you are walking {0}km and it will take {1}hours".format(distance, formatedTime))


angle = math.atan2(yDiff, xDiff)
print("The angle calculates is {:0.2f} radians".format(angle))


print("{theAnswer:12.5f}".format(TheAnswer=123.456))