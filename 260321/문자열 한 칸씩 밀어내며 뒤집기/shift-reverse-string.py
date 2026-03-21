import sys

input = sys.stdin.readline

# 선언부
def solve(s: str, api: int):
    if api == 1:
        s = s[1:] + s[0]
    elif api == 2:
        s = s[-1] + s[:-1]
    elif api == 3:
        s = s[::-1]
    return s

# 구현부
s, Q = input().rstrip().split()
Q = int(Q)
for _ in range(Q):
    api = int(input())
    s = solve(s, api)
    print(s)
