##def factorial(n):
##    result = n
##    for i in range(1, n):
##        result *= i
##    return result

#阶乘
def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)

#幂
def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n-1)

