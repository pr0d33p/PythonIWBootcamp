string1 = "abc"
string2 = "xyz"

newString1 = string2[:2] + string1[2:]
newString2 = string1[:2] + string2[2:]

print(newString1 + ' ' + newString2)