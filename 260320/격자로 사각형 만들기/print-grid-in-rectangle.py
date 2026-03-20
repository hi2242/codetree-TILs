import sys

input = sys.stdin.readline

# 선언부
def print_grid(grid: list[list[int]]):
    for row in grid:
        print(*row)

def solve(n: int):
    grid = [[1 for _ in range(n)] for _ in range(n)]
    for r in range(1, n):
        for c in range(1, n):
            grid[r][c] = grid[r - 1][c] + grid[r][c - 1] + grid[r - 1][c - 1]
    print_grid(grid)

# 구현부
N = int(input())
solve(N)
