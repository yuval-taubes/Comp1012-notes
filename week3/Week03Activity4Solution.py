#COMP 1012 Week 3 Activity 4

TRUCK_VOLUME = 8
TOLERANCE = 4 #how much leftover is enough to make an extra trip
LG_ORDER_COST = 10 #cost per cubic metre
LG_ORDER_LIMIT = 50 #number of cubic metres required to get lg soil cost
MED_ORDER_COST = 20
MED_ORDER_LIMIT = 20
SM_ORDER_COST = 30

LG_DELIVERY_COST = 80 #cost per truck for a large order
LG_DELIVERY_LIMIT = 10 #number of loads required to get lg delivery cost
SM_DELIVERY_COST = 100

TAX_RATE = 0.12

volumeString = "invalid"
while not volumeString.isnumeric():
    volumeString = input("Please enter the number of cubic metres of soil to be purchased: ")

#exited loop, must be numeric & can cast
volumeDesired = int(volumeString)

numLoads = volumeDesired // TRUCK_VOLUME #integer division
volumeSold = numLoads * TRUCK_VOLUME

if volumeDesired % TRUCK_VOLUME >= TOLERANCE:
    numLoads = numLoads + 1
    volumeSold = volumeSold + volumeDesired % TRUCK_VOLUME

# set the cost per cubic metre    
if volumeSold >= LG_ORDER_LIMIT:
    costPerCubicM = LG_ORDER_COST
elif volumeSold >= MED_ORDER_LIMIT:
    costPerCubicM = MED_ORDER_COST
else:
    costPerCubicM = SM_ORDER_COST
    
# set the cost per load
if numLoads >= LG_DELIVERY_LIMIT:
    costPerLoad = LG_DELIVERY_COST
else:
    costPerLoad = SM_DELIVERY_COST

# calculate total
totalCost = costPerCubicM * volumeSold + costPerLoad * numLoads

# add tax
totalCost = totalCost * (1 + TAX_RATE)

output = "The cost of buying and transporting {:d} cubic metres in {:d} loads is ${:.2f}."
output = output.format(volumeSold, numLoads, totalCost)

print(output)