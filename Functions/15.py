numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evenNumbers = list(filter(lambda x: x%2 == 0, numbers))
print("Even Numbers: {}".format(evenNumbers))
oddNumbers = list(filter(lambda x: x%2 != 0, numbers))
print("Odd Numbers: {}".format(oddNumbers))
