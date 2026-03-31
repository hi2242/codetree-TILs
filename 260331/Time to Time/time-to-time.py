import sys

input = sys.stdin.readline

# 선언부
def solve(start_h: int, start_m: int, end_h: int, end_m: int):
    print((end_h - start_h) * 60 + end_m - start_m)
    
# 구현부
A, B, C, D = map(int, input().split())
solve(A, B, C, D)
