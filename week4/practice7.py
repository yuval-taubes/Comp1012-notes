import math
# data = [8, 19, 53, 27, 31, 82, 16, 72, 3, 22]
data = [4, 4]
sqrt_data = []
product = 0
for i in data:
    sqrt_i = math.sqrt(i)
    sqrt_data.append(sqrt_i)

product = math.prod(sqrt_data)

print(product)