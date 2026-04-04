import sys

input = sys.stdin.readline

# 선언부
def print_extend(grid: list[list[int]], x1: int, y1: int, x2: int, y2: int):
    max_width, max_height = 0, 0
    temp1, temp2 = 0, 0
    for c in range(x1, x2):
        if grid[y1 + 1000][c + 1000] == 1:
            temp1 += 1
        if grid[y2 + 1000 - 1][c + 1000] == 1:
            temp2 += 1
    else:
        if temp1 == temp2:
            max_width = x2 - x1
        else:
            max_width = max(temp1, temp2)
        temp1, temp2 = 0, 0

    for r in range(y1, y2):
        if grid[r + 1000][x1 + 1000] == 1:
            temp1 += 1
        if grid[r + 1000][x2 + 1000 - 1] == 1:
            temp2 += 1
    else:
        if temp1 == temp2:
            max_height = y2 - y1
        else:
            max_height = max(temp1, temp2)
    print(max_width * max_height)

def solve(x1: int, y1: int, x2: int, y2: int, i: int):
    for r in range(y1, y2):
        for c in range(x1, x2):
            grid[r + 1000][c + 1000] = i

# 구현부
grid = [[0 for _ in range(2001)] for _ in range(2001)]
fx1, fy1, fx2, fy2 = map(int, input().split())
solve(fx1, fy1, fx2, fy2, 1)
sx1, sy1, sx2, sy2 = map(int, input().split())
solve(sx1, sy1, sx2, sy2, 2)
print_extend(grid, fx1, fy1, fx2, fy2)