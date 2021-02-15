sampleWords = input("Enter the words separated by comma: ")

individualWords = sampleWords.split(",")

listWord = []

for word in individualWords:
    listWord.append(word.strip())

final = sorted(set(listWord))

print(', '.join(final))