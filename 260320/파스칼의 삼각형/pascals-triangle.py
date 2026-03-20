import sys

input = sys.stdin.readline

# 선언부
def print_grid(n: int, grid: list[list[int]]):
    for r in range(n):
        for c in range(n):
            if r < c:
                continue
            print(grid[r][c], end=' ')
        print()

def solve(n: int):
    grid = [[1 for _ in range(n)] for _ in range(n)]
    for r in range(1, n):
        for c in range(1, n):
            if r <= c:
                continue
            grid[r][c] = grid[r - 1][c] + grid[r - 1][c - 1]
    print_grid(n, grid)

# 구현부
N = int(input())
solve(N)
