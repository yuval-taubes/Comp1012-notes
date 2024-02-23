#COMP 1012 Week 4 Activity 3

#two ordered lists
list1 = [3, 12, 18, 23, 26, 31, 34, 40]
list2 = [5, 8, 10, 11, 18, 23, 29]


print("The numbers that are found in both lists are:")
index1 = 0
index2 = 0
while index1 < len(list1) and index2 < len(list2):  #if both indices are in bounds
    if list1[index1] == list2[index2]: #if there is a match
        print(list1[index1]) #could print from either list
        index1 += 1
        index2 += 1
    elif list1[index1] < list2[index2]:  #current number in list1 is smaller - that number can't be in list2 (we would have seen it already)
        index1 += 1
    else:  #must be current number in list2 that is smaller
        index2 += 1
#one list was processed fully - we don't need to finish the other list because it can't possibly have any matches
    
    
print("The numbers found in one but not both lists are:")
index1 = 0
index2 = 0
while index1 < len(list1) and index2 < len(list2):  #if both indices are in bounds
    if list1[index1] == list2[index2]: #if there is a match
        #skip printing
        index1 += 1
        index2 += 1
    elif list1[index1] < list2[index2]:  #current number in list1 is smaller - can't possibly have a match
        print(list1[index1])
        index1 += 1
    else:  #current number in list2 is smaller - doesn't have a match
        print(list2[index2])
        index2 += 1

#finish printing the list that was not done
while index1 < len(list1):
    print(list1[index1])
    index1 += 1
while index2 < len(list2):
    print(list2[index2])
    index2 += 1


print("The combined list is:")
index1 = 0
index2 = 0
list3 = [] #empty list
while index1 < len(list1) and index2 < len(list2):  #if both indices are in bounds
    if list1[index1] == list2[index2]: #if there is a match, copy both
        list3.append(list1[index1])
        list3.append(list2[index2])
        index1 += 1
        index2 += 1
    elif list1[index1] < list2[index2]:  #current number in list1 is smaller
        list3.append(list1[index1])
        index1 += 1
    else:  #must be current number in list2 that is smaller
        list3.append(list2[index2])
        index2 += 1
        
#finish copying the list that was not done
while index1 < len(list1):
    list3.append(list1[index1])
    index1 += 1
while index2 < len(list2):
    list3.append(list2[index2])
    index2 += 1

print(list3)


print("NOTE: Appending one list to the other:")
unsorted = list1+list2
print(unsorted)  #note that this appends list2 to the end of list1 - it does not sort the values in the resulting list