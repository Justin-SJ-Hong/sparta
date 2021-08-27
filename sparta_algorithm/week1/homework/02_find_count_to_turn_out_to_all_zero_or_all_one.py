input = "101010"

def find_count_to_turn_out_to_all_zero_or_all_one(string):
    # count_to_all_zero, count_to_all_one는 0으로 초기화
    count_to_all_zero = 0
    count_to_all_one = 0

    # 0으로 시작할 경우 count_to_all_one의 값은 1 증가(최대 1번 비교)
    if string[0] == '0':
        count_to_all_one += 1
    # 1으로 시작할 경우 count_to_all_zero의 값은 1 증가(최대 1번 비교)
    elif string[0] == '1':
        count_to_all_zero += 1

    for i in range(len(string) - 1): # 0부터 len(string) - 2까지 i값을 증가시킴(최대 n-1번 비교)
        if string[i] != string[i + 1]: # 해당 숫자가 다음 인덱스에서도 반복되지 않을 때만 발동
            if string[i + 1] == '0': # 해당 숫자가 1에서 0으로 변경
                count_to_all_one += 1 # count_to_all_one의 값을 1씩 증가
            if string[i + 1] == '1': # 해당 숫자가 0에서 1로 변경
                count_to_all_zero += 1 # count_to_all_zero의 값을 1씩 증가

    return min(count_to_all_one, count_to_all_zero)


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)