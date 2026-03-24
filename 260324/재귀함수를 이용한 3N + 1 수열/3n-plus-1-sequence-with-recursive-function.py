import sys

input = sys.stdin.readline

# 선언부
def solve(n: int):
    if n == 1:
        return 0
    return (solve(n // 2) if n % 2 == 0 else solve(n * 3 + 1)) + 1

# 구현부
N = int(input())
print(solve(N))
