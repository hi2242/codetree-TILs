import sys

input = sys.stdin.readline

# 선언부
def translate(s: str):
    temp = ''
    for c in s:
        if '0' <= c <= '9':
            temp += c
        else:
            break
    return int(temp)

# 구현부
s1, s2 = input().rstrip().split()
a, b = translate(s1), translate(s2)
print(a + b)
