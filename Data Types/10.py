word = "python"

newWord = ''

for i in range(0, len(word)):
    if i % 2 == 0:
        newWord += word[i]
    else:
        newWord += ''

print(newWord)