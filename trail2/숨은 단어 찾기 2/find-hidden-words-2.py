import sys

input = sys.stdin.readline

# 선언부
def print_grid(grid: list[list[int]]):
    for row in grid:
        print(*row)

def check():

def solve():
    for r in range(N):
        for c in range(M):
            for i in range(8):
                if grid[r][c] == 'L' and grid[r + dr[i]][c + dc[i]]
            if grid[r][c] == 'L':
                check()
# 구현부
N, M = map(int, input().split())
grid = [list(input().rstrip()) for _ in range(N)]
dr, dc = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]
print_grid(grid)
solve()
