array_a = [1, 2, 3, 5]
array_b = [4, 6, 7, 8]


def merge(array1, array2):
    array_c = []
    i = 0
    j = 0
    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            array_c.append(array1[i])
            i += 1
        else:
            array_c.append(array2[j])
            j += 1
    if i == len(array1):
        while j < len(array2):
            array_c.append(array2[j])
            j += 1

    if j == len(array2):
        while i < len(array1):
            array_c.append(array1[i])
            i += 1

    return array_c


print(merge(array_a, array_b))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!