import sys

input = sys.stdin.readline

# 선언부
def solve(s: str):
    info = ['No', 'No']
    for i in range(len(s) - 1):
        if s[i] == 'e' and s[i + 1] == 'e':
            info[0] = 'Yes'
        elif s[i] == 'a' and s[i + 1] == 'b':
            info[1] = 'Yes'
    print(*info)

# 구현부
s = input().rstrip()
solve(s)
