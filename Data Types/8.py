string = "Hello, World"

strToRemove = 5

newString = ''

if len(string) > 0:
    for letter in string:
        if letter == string[strToRemove]:
            newString += ''
        else:
            newString += letter

    print(newString)