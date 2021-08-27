# 재귀 함수는 재귀 연산의 수가 많아질 수록 효율이 떡락한다.(부분문제 발생)

input = 100


def fibo_recursion(n):
    if n == 1 or n == 2:
        return 1
    return fibo_recursion(n - 1) + fibo_recursion(n - 2)


print(fibo_recursion(input))  # 6765