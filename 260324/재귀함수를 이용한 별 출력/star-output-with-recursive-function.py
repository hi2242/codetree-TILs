import sys

input = sys.stdin.readline

# 선언부
def solve(n: int):
    if n == 0:
        return
    solve(n - 1)
    print('*' * n)
    
# 구현부
N = int(input())
solve(N)
