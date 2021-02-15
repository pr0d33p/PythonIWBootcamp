num = int(input("Enter a number to find factorial: "))

def calculateFactorial(num):
    factorial = 1

    if num < 0:
        print("The program is not for negative integers.");
        exit(0)
    elif(num == 0):
        return ("1");
    else:
        while(num > 0):
            factorial = factorial * num
            num = num - 1
    return factorial

print("The factorial of given number is: {}".format(calculateFactorial(num)))