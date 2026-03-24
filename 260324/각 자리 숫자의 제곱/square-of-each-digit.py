import sys

input = sys.stdin.readline

# 선언부
def solve(n: int):
    if n == 0:
        return 0

    return solve(n // 10) + (n % 10) ** 2

# 구현부
N = int(input())
print(solve(N))
