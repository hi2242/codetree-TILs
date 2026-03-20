import sys

input = sys.stdin.readline

# 선언부
def print_grid(grid: list[list[int]]):
    for row in grid:
        print(*row)

def solve():
    grid = [[1 for _ in range(5)] for _ in range(5)]
    for r in range(1, 5):
        for c in range(1, 5):
            grid[r][c] = grid[r - 1][c] + grid[r][c - 1]
    
    print_grid(grid)
    
# 호출부
solve()
