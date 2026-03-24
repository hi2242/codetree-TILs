import sys

input = sys.stdin.readline

# 선언부
def solve(s: str):
    n = len(s)
    for i in range(n // 2):
        if s[i] != s[n - 1 - i]:
            print('No')
            break
    else:
        print('Yes')

# 구현부
s = input().rstrip()
solve(s)
