import sys

input = sys.stdin.readline

# 선언부
def print_extend(grid: list[list[int]]):
    count = 0
    for r in range(201):
        for c in range(201):
            if grid[r][c] == 0:
                count += 1
    print(count)

def solve(x1: int, y1: int, x2: int, y2: int, i: int):
    for r in range(y1, y2):
        for c in range(x1, x2):
            grid[r + 100][c + 100] = i

# 구현부
N = int(input())
grid = [[-1 for _ in range(201)] for _ in range(201)]
for i in range(1, N + 1):
    x1, y1, x2, y2 = map(int, input().split())
    solve(x1, y1, x2, y2, i % 2)
print_extend(grid)