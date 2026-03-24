import sys

input = sys.stdin.readline

# 선언부
def solve(s: str):
    result = 'No'
    for i in range(len(s) - 1):
        if s[i] != s[i + 1]:
            result = 'Yes'
    print(result)

# 구현부
A = input().rstrip()
solve(A)
