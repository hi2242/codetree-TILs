import sys

input = sys.stdin.readline

# 선언부
def solve(start: int, end: int):
    acc = 0
    for i in range(a, b + 1):
        if i % 2 == 0:
            acc += i
    return acc

# 구현부
N = int(input())
for _ in range(N):
    a, b = map(int, input().split())
    print(solve(a, b))