import sys

input = sys.stdin.readline

# 선언부
def calc_width(grid: list[list[int]], x1: int, x2: int, y: int) -> int:
    temp, start, stop = 0, False, False
    for c in range(x1, x2):
        if grid[y + 1000][c + 1000] == 1:
            if start and stop:
                temp = x2 - x1
                break
            temp += 1
            start = True
        else:
            if start == True:
                stop = True
    return temp

def calc_height(grid: list[list[int]], y1: int, y2: int, x: int) -> int:
    temp, start, stop = 0, False, False
    for r in range(y1, y2):
        if grid[r + 1000][x + 1000] == 1:
            if start and stop:
                temp = y2 - y1
                break
            temp += 1
            start = True
        else:
            if start == True:
                stop = True
    return temp

def print_extend(grid: list[list[int]], x1: int, y1: int, x2: int, y2: int):
    max_width, max_height = 0, 0
    temp1 = calc_width(grid, x1, x2, y1)
    temp2 = calc_width(grid, x1, x2, y2 - 1)
    max_width = max(temp1, temp2)

    temp1 = calc_height(grid, y1, y2, x1)
    temp2 = calc_height(grid, y1, y2, x2 - 1)
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
