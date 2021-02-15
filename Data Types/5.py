string = "string"

if len(string) >= 3:
    if string[-3:] != 'ing':
        string = string + 'ing'
    else:
        string = string + 'ly'

print(string)