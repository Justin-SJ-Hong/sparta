input = "abacabade"


def find_not_repeating_character(string):
    alphabet_occurrence_array = [0] * 26

    # 각 문자에 따른 arr_index를 구함
    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord("a")
        alphabet_occurrence_array[arr_index] += 1
    not_repeating_character_array = []
    for index in range(len(alphabet_occurrence_array)):
        alphabet_occurrence = alphabet_occurrence_array[index]
        if alphabet_occurrence == 1: # 반복되는 횟수에 해당하는 알파벳을 찾음(만약 alphabet_occurrence의 값이 2일 경우 2번 반복하는 알파벳을 찾는다.
            not_repeating_character_array.append(chr(index + ord("a")))

    print(not_repeating_character_array)
    for char in string:
        if char in not_repeating_character_array:
            return char
    return "_"


result = find_not_repeating_character(input)
print(result)