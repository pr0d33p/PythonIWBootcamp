def calculate(num):
    return lambda res : res * num

result = calculate(2)
print("Double the number of 12 =", result(12))

result = calculate(3)
print("Triple the number of 12 =", result(12))