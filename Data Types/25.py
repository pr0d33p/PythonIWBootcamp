dic =  [{},{},{}]

res = []

for item in dic:
    if (len(item)) == 0:
        res.append(True)
    else:
        res.append(False)

print(all(res))