# your code goes here
def triple(x):
    if isinstance(x, int):  # x가 정수인지 확인
        result = x * 3
    elif isinstance(x, str) and x.isdigit():  # x가 숫자 형태의 문자열인지 확인
        result = int(x) * 3
    else:
        result = x + x + x  # 일반 문자열일 경우
    return result

print(triple(3))       # 9
print(triple("3"))     # 9
print(triple("abc"))