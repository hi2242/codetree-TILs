import sys

input = sys.stdin.readline

# 선언부
def pick_number(s: str):
    temp = ''
    for c in s:
        if '0' <= c <= '9':
            temp += c
    
    return int(temp)

# 구현부
s1 = input().rstrip()
s2 = input().rstrip()

print(pick_number(s1) + pick_number(s2))
