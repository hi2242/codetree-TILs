import sys

input = sys.stdin.readline

# 선언부
def print_grid(grid: list[list[int]]):
    for row in grid:
        print(*row)

def solve(n: int, p_list: list[list[int]]):
    grid = [[0 for _ in range(n)] for _ in range(n)]
    for r, c in p_list:
        grid[r - 1][c - 1] = r * c
    print_grid(grid)

# 구현부
N, M = map(int, input().split())
point_list = []
for _ in range(M):
    r, c = map(int, input().split())
    point_list.append((r, c))
solve(N, point_list)
