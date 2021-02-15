string = "The quick Brow Fox"

def countUpperLower(string):

    lowerCaseCount = 0
    upperCaseCount = 0

    for letter in string:
        if letter.isupper():
            upperCaseCount += 1
        elif letter.islower():
            lowerCaseCount += 1

    print("No. of Upper case characters: {}".format(upperCaseCount))
    print("No. of Lower case Characters: {}".format(lowerCaseCount))


countUpperLower(string)