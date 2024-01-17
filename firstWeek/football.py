import math
velocity = 19 #m/s
goalpost_distance = 30
degree = math.pi / 4

time = goalpost_distance / (velocity * math.cos(degree))

# 𝑦 = 𝑣 ∗ sin(𝜃) ∗ 𝑡 − 0.5 ∗ 𝑔 ∗ 𝑡2

height = (velocity * math.sin(degree) * time) - (0.5 * 9.8 * time**2)

print("the height of the ball at the goalpost is {:0.2f}".format(height))