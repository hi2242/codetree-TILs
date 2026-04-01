import sys

input = sys.stdin.readline

# 선언부
def solve(A: int, B: int, C: int):
    result = -1
    if A > 11 or (A == 11 and B > 11) or (A == 11 and B == 11 and C >= 11):
        result = (A - 11) * 24 * 60 + (B - 11) * 60 + (C - 11)
    print(result)

# 구현부
A, B, C = map(int, input().split())
solve(A, B, C)
