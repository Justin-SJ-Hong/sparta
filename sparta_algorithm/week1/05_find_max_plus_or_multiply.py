input = [0, 3, 5, 6, 1, 2, 4] # N = 7

def find_max_plus_or_multiply(array):
    multiply_sum = 0
    for number in array: # N회 비교(빅오는 N)
        if number <= 1 or multiply_sum <= 1: # array의 인덱스 값이 0 또는 1일 때 왜 더하는걸까? 만약 input 배열이 [3, 8, 5, 6, 1, 2, 4]로 배치되어 있다면 3 * 8 = 24가 3 + 8 = 11보다 더 클텐데...
            multiply_sum += number
        else:
            multiply_sum *= number
    return multiply_sum

result = find_max_plus_or_multiply(input)
print(result)