# 이진 탐색은 배열이 순차적으로 정렬되어 있지 않을 경우 절대로 탐색이 불가능하다.
# 이진 탐색을 수행하기 전에는 순차적으로 정렬하는 절차를 반드시 거쳐야 한다.

finding_target = 2
finding_numbers = [0, 3, 5, 6, 1, 2, 4]


def is_exist_target_number_binary(target, numbers):
    find_count = 0
    for num in numbers:
        find_count += 1
        if target == num:
            print(find_count)
            return True
    return False


result = is_exist_target_number_binary(finding_target, finding_numbers)
print(result)
