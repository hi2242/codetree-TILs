import sys

input = sys.stdin.readline

# 선언부
def solve(n: int):
    if n == 1:
        return 0
    if n % 2 == 0:
        n //= 2
    else:
        n //= 3

    return solve(n) + 1

# 구현부
N = int(input())
print(solve(N))
