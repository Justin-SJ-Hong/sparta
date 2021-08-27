# n! = n * (n - 1)!

def factorial(n):
    if n == 1:
        return 1
    # n이 1이 아닌 경우 n * (n - 1)!을 반복 수행함
    return n * factorial(n - 1)



print(factorial(5))