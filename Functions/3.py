def multiplyInList(list):
    totalProd = 1
    for number in list:
        totalProd *= number
    return totalProd

print(multiplyInList([8, 2, 3, -1, 7]))