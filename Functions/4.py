def reverseString(string):
    strToReturn = ""
    for letter in string:
        strToReturn = letter + strToReturn

    return strToReturn

print(reverseString("Hello"))