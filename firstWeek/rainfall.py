waterCollectionArea=100 #km^2
lakeCompArea=2 #km^2
raiseLakeBy=1 #m

# 100 000 * height of rain needed = lakeCompArea

rainNeeded = (lakeCompArea * raiseLakeBy)/ (waterCollectionArea)
rainNeeded_mm = rainNeeded/ 0.001
print("you need {}mm of rain to raise the level of the lake by {}m".format(rainNeeded_mm, raiseLakeBy))




num = 123456789 % 10

print(num)