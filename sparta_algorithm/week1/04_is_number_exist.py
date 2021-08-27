input = [3, 5, 6, 1, 2, 4] # N = 6


def is_number_exist(number, array):
    # 이 부분을 채워보세요!
    for element in array: # array 길이 N만큼 아래 연산 실행
        if number == element: # 비교연산 1회 실행
            return True # 최소 1회(빅오메가), 최대 N * 1 = N회만큼 비교(빅오, 알고리즘은 항상 빅오를 고려함)
    return False # for문 돌려도 반환 못함


result = is_number_exist(3, input) # input 배열에 숫자 number가 존재하면 True, 아니면 False
print(result) # 결과값 출력