import sys

input = sys.stdin.readline

# 선언부
def print_grid(grid: list[list[int]]):
    for row in grid:
        print(*row)

def solve(n: int, m: int):
    grid = [[0 for _ in range(m)] for _ in range(n)]
    count = 1
    for i in range(n + m):
        for j in range(i + 1):
            if j >= n or i - j >= m:
                continue
            grid[j][i - j] = count
            count += 1

    print_grid(grid)

# 구현부
N, M = map(int, input().split())
solve(N, M)
