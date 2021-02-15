def checkInRange(number, start, end):
    if number >= start and number < end:
        return "The number is in range."
    return "The number is not in range."

print(checkInRange(5, 10, 15))
print(checkInRange(5, 1, 15))