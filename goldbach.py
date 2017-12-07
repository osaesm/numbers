import math

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

def goldbach(n):
    for i in range(2,n - 1):
        j = n - i
        if (isPrime(i) and isPrime(j)):
            return True
    return False


def runGoldbach(n):
    for i in range(4, n + 1, 2):
        if (not goldbach(i)):
            return str(i)
            break
        if (i % (n / 10) == 0):
            print(i)
    return("True up to", n)

print(runGoldbach(10 ** 6))