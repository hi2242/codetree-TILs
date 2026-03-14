import sys

input = sys.stdin.readline

# 선언부
def solve(start: int, end: int):
    prod = 1
    for i in range(a, b + 1):
        prod *= i
    return prod

# 구현부
N = int(input())
for _ in range(N):
    a, b = map(int, input().split())
    print(solve(a, b))


