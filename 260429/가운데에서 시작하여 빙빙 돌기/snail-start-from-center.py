import sys

input = sys.stdin.readline

# 선언부
def print_grid(grid: list[list[int]]):
    for row in grid:
        print(*row)

def validate(r: int, c: int):
    return (
        0 <= r < N and 
        0 <= c < N
    )

def solve() -> None:
    cr = cc = N // 2
    direction = 0
    count = 1
    can_move = 0
    dr, dc = [0, -1, 0, 1], [1, 0, -1, 0]

    grid[cr][cc] = count
    count += 1
    while True:
        if direction == 0 or direction == 2:
            can_move += 1
        for _ in range(can_move):
            if count > N * N:
                print_grid(grid)
                return
            cr, cc = cr + dr[direction], cc + dc[direction]
            grid[cr][cc] = count
            count += 1
        direction = (direction + 1) % 4

# 구현부
N = int(input())
grid = [[0 for _ in range(N)] for _ in range(N)]
solve()
