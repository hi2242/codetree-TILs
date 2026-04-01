import sys

input = sys.stdin.readline

# 선언부
def solve(A: int, B: int, C: int):
    result = 0
    result = (A - 11) * 24 * 60 + (B - 11) * 60 + (C - 11)
    print(result)
    
# 구현부
A, B, C = map(int, input().split())
solve(A, B, C)
