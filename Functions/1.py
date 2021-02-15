a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

def greatestNum(a, b, c):

    greatest = 0
    if (a >= b) and (a >= c):
        greatest = a
    elif (b >= a) and (b >= c):
        greatest = b
    else:
        greatest = c
    
    return greatest

print("The greatest number is: {}".format(greatestNum(a, b, c)))