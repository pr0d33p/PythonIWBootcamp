def insert_sting_middle(string, item):
    middlePlace = int(len(string)/2)
    startingStr = string[:middlePlace]
    endingStr = string[middlePlace:]
    finalWord = startingStr + item + endingStr
    return finalWord

print(insert_sting_middle('[[]]', 'Python'))
print(insert_sting_middle('{{}}', 'PHP'))