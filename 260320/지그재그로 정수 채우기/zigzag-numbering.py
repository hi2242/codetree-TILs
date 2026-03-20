import sys

input = sys.stdin.readline

# 선언부
def print_grid(grid: list[list[int]]):
    for row in grid:
        print(*row)

def solve(n: int, m: int):
    grid = [[0 for _ in range(m)] for _ in range(n)]
    count = 0
    for c in range(m):
        if c % 2 == 0:
            for r in range(n):
                grid[r][c] = count
                count += 1
        else:
            for r in range(n - 1, -1, -1):
                grid[r][c] = count
                count += 1

    print_grid(grid)

# 구현부
N, M = map(int, input().split())
solve(N, M)