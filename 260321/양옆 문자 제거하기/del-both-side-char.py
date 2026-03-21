import sys

input = sys.stdin.readline

# 선언부
def solve(s: str):
    a = list(s)
    a.pop(1)
    a.pop(-2)
    print(*a, sep='')

# 구현부
s = input().rstrip()
solve(s)
