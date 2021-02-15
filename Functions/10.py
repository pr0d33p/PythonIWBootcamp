def checkEven(inpList):
    retList = []
    for number in inpList:
        if number % 2 == 0:
            retList.append(number)
    
    return retList

print(checkEven([1, 2, 3, 4, 5, 6, 7, 8, 9]))