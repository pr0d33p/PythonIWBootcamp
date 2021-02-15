list = [9, 1, 5, 8, 19, 11, 3]

smallestNum = list[0]

for item in list:
    if(smallestNum > item):
        smallestNum = item
    

print(smallestNum)