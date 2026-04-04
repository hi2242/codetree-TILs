import sys

input = sys.stdin.readline

# 선언부
def print_extend(grid: list[list[int]]):
    count = 0
    for r in range(201):
        for c in range(201):
            if grid[r][c] == 1:
                count += 1
    print(count)

def solve(x: int, y: int):
    for r in range(y, y + 8):
        for c in range(x, x + 8):
            grid[r + 100][c + 100] = 1

# 구현부
N = int(input())
grid = [[0 for _ in range(201)] for _ in range(201)]
for _ in range(N):
    x, y = map(int, input().split())
    solve(x, y)
print_extend(grid)
