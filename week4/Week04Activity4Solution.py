#COMP 1012 Week 4 Activity 4

myFile = open("Week4Houses.csv")  #address, number sq ft, selling price

#create empty lists to store data
addressList = []
sizeList = []
priceList = []

mostExpensive = 0 #set to any value that guarantees the first house will be more expensive
mostIndex = -1  #position in lists where most expensive house is stored

leastExpensive = 1000000000 #set to any value that guarantees the first house will be cheaper
leastIndex = -1  #position in lists where cheapest house is stored

#load data into parallel lists
for line in myFile:
    items = line.split(',')
    addressList.append(items[0].strip())
    sizeList.append(float(items[1].strip()))
    priceList.append(float(items[2].strip()))

myFile.close()

#print list of houses
#and search for the most expensive and least expensive
for i in range(len(addressList)):
    pricePerSqFt = priceList[i] / sizeList[i]
    output = "{} costs ${:.2f} per square foot."
    print(output.format(addressList[i],pricePerSqFt))
    
    if pricePerSqFt > mostExpensive:  #current house is more expensive than any seen previously
        mostExpensive = pricePerSqFt
        mostIndex = i
        
    if pricePerSqFt < leastExpensive:  #current house is cheaper than any seen previously
        leastExpensive = pricePerSqFt
        leastIndex = i

output = "\nThe least expensive house is at {}. With {:.0f} sq ft and a selling price of ${:.2f}, the price per square foot is ${:.2f}"
print(output.format(addressList[leastIndex], sizeList[leastIndex], priceList[leastIndex], leastExpensive))

output = "\nThe most expensive house is at {}. With {:.0f} sq ft and a selling price of ${:.2f}, the price per square foot is ${:.2f}"
print(output.format(addressList[mostIndex], sizeList[mostIndex], priceList[mostIndex], mostExpensive))
