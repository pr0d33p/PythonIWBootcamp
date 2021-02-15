def findLongestWord(list):

    longestWord = list[0]

    for word in list:
        if len(longestWord) < len(word):
            longestWord = word

    return len(longestWord)

print(findLongestWord(['one', 'two', 'three', 'four']))