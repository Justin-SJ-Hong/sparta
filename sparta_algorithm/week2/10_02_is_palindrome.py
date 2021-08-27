#재귀 함수는 문제 규모가 축소되어야 함

input = "가지고고지가"


def is_palindrome(string):
    # 문자열의 문자 수가 홀수개인 경우 string 길이가 1, 짝수개인 경우 string 길이가 0일 때 True를 반환
    if len(string) <= 1:
        return True
    # 맨앞하고 맨뒤가 서로 다르면 False를 반환
    if string[0] != string[-1]:
        return False
    # 맨앞 그리고 맨뒤를 자름
    return is_palindrome(string[1: -1])


print(is_palindrome(input))
