import sys

input = sys.stdin.readline

# 선언부
def print_extend(grid: list[list[int]]):
    count = 0
    for r in range(2001):
        for c in range(2001):
            if grid[r][c] == 1:
                count += 1
    print(count)

def solve(x1: int, y1: int, x2: int, y2: int, i: int):
    for r in range(y1, y2):
        for c in range(x1, x2):
            if i != 3:
                grid[r + 1000][c + 1000] = 1
            else:
                grid[r + 1000][c + 1000] = 0

# 구현부
grid = [[0 for _ in range(2001)] for _ in range(2001)]
for i in range(1, 4):
    x1, y1, x2, y2 = map(int, input().split())
    solve(x1, y1, x2, y2, i)
print_extend(grid)
