import sys

input = sys.stdin.readline

# 선언부
def print_grid(grid: list[list[int]]):
    for row in grid:
        print(*row)

def solve(n: int, m: int, p_list: list[list[int]]):
    grid = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(m):
        r, c = p_list[i]
        grid[r - 1][c - 1] = i + 1

    print_grid(grid)

# 구현부
N, M = map(int, input().split())
point_list = []
for _ in range(M):
    r, c = map(int, input().split())
    point_list.append((r, c))
solve(N, M, point_list)
