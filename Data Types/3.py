string = "restart"

character = string[0]

str = string.replace(character, '$')
str = character + str[1:]

print(str)