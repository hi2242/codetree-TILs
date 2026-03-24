import sys

input = sys.stdin.readline

# 선언부
def solve(n: int):
    if n == 1 or n == 2:
        return 1
    return solve(n - 1) + solve(n - 2)
    
# 구현부
N = int(input())
print(solve(N))
