# 소수는 2부터 시작한다.

input = 20


def find_prime_list_under_number(number):
    # 이 부분을 채워보세요!
    prime_list = [] # 배열 선언
    for n in range(2, number + 1): # 2부터 number까지 n값을 1씩 증가시키면서 비교함(최대 n-2번 비교)
        for i in range(2, n): # 2부터 n-1까지 i값을 1씩 증가시키면서 비교함(최대 n-3번 비교)
            if n % i  == 0: # n을 i로 나눈 결과 0이 나올 경우 for i in range(2, n)을 탈출(최대 1번 비교)
                break
        # i값이 n값과 동일할 경우 else문을 발동하여 prime_list에 추가한다.
        else:
            prime_list.append(n)
    return prime_list

# 이 코드에서 find_prime_list_under_number(number) 함수는 input의 값을 매개변수로 받음
result = find_prime_list_under_number(input)
print(result)