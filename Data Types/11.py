dictionary = {}

sentence = "the quick brown fox jumps over the lazy dog.".lower()

words = sentence.split()

for word in words:
    key = dictionary.keys()
    if word in key:
        dictionary[word] += 1
    else:
        dictionary[word] = 1

print(dictionary)    