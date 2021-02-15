def checkPrime(num):
    counter = 0

    if num == 0 or num == 1:
        print("The number is neither prime nor composite")
        exit(0)
    elif num == 2:
        print("The number is prime.")
        exit(0)
    else:
        n = 2
        while num > n:
            if (num % n) == 0:
                print("The number is composite")
                exit(0)
            else:
                n+=1

    print("The number is prime.")

checkPrime(5)