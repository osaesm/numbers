def factorial(n):
    if n < 2:
        return 1
    product = 1
    for i in range(1,n+1):
        product *= i
    return product

def pi(n):
    sum = 0
    for i in range(n):
        sum += (factorial(6*i) * (13591409 + 545140134 * i))/(factorial(3*i) * (factorial(i) ** 3) * (-640320) ** (3*i))
    sum *= 12 / (640320 ** 1.5)
    sum = sum ** -1
    print(sum)

pi(1000)