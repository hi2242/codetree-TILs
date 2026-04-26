import sys

input = sys.stdin.readline

# 선언부
def print_grid(grid: list[list[int]]):
    for row in grid:
        print(*row)

def validate(r: int, c: int):
    return 0 <= r < N and 0 <= c < M

def solve():
    direction = 0
    curr = 1
    nr, nc = 0, 0
    while True:
        if curr > N * M:
            break
        grid[nr][nc] = curr
        curr += 1
        if not (validate(nr + dr[direction], nc + dc[direction]) and grid[nr + dr[direction]][nc + dc[direction]] == 0):
            direction = (direction + 1) % 4
        nr, nc = nr + dr[direction], nc + dc[direction]
    print_grid(grid)

# 구현부
N, M = map(int, input().split())
grid = [[0 for _ in range(M)] for _ in range(N)]
dr, dc = [1, 0, -1, 0], [0, 1, 0, -1]
solve()
