#area of a triangle

height = 10
width = 5

def CalcTriangleArea(height, width):
    return (height * width) / 2

triangleArea = CalcTriangleArea(height, width)

print("The area of the triangle is {}".format(triangleArea))

# convert miles to km

mileDistnace = 16

def ConvertMileToKm(mile):
    return mile * 1.61

kmDistance = ConvertMileToKm(mileDistnace)

print("The distnace in km is {:0.2f}".format(kmDistance))

# string - name, sport, day

name = "John Doe"
sport = "Football"
day = "Monday"

print("{} played {} on {}".format(name, sport, day))

var = 1 % 3
var2 = 2 % 3
var3 = 3 % 3
var4 = 4 % 3
var5 = 5 % 3
var6 = 6 % 3
var7 = 7 % 3
var8 = 8 % 3
var9 = 9 % 3
var10 = 10 % 3


print(var)
print(var2)
print(var3)
print(var4)
print(var5)
print(var6)
print(var7)
print(var8)
print(var9)
print(var10)

x=3
y=4

output = "D1v1ding gives{c: .4f} and multiplying gives{b:6.2f}"
prettyoutput = output.format(b=x*y, c=x/y)
print(prettyoutput)