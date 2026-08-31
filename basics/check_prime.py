import math
def checkPrime():

    numbercheck = int(input("pls enter a number"))
    sqRoot = math.isqrt(numbercheck)
    for i in range(2, sqRoot + 1):
        if numbercheck % i == 0:
            print("The number is not prime")
            break
        else:
            print("The number is prime")
            break
checkPrime()
""" num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")


 """