import sys

input = sys.stdin.readline

# 선언부
def solve(x1: int, x2: int, lines: list[int]):
    for i in range(x1, x2 + 1):
        lines[i] += 1

# 구현부
N = int(input())
lines = [0 for _ in range(101)]
for _ in range(N):
    x1, x2 = map(int, input().split())
    solve(x1, x2, lines)
print(max(lines))
