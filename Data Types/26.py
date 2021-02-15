list = [1, 2, 3, 4]

string = "emp"

newList = []

for item in list:
    newList.append(string+"{}".format(item))

print(newList)