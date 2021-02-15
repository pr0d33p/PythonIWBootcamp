list = [1, 5, 8, 19, 11, 3]

largestNum = list[0]

for item in list:
    if(item > largestNum):
        largestNum = item
    

print(largestNum)