import sys

input = sys.stdin.readline

# 선언부
def print_grid(grid: list[list[int]]):
    for row in grid:
        print(*row)

def get_next_alphabet(target: str, difference: int):
    return chr(ord(target) + difference)

def validate_range(r: int, c: int):
    return 0 <= r < N and 0 <= c < M and grid[r][c] == 0

def solve():
    direction, count, difference = 0, 0, 0
    initial_alphabet = 'A'
    dr, dc = [0, 1, 0, -1], [1, 0, -1, 0]
    cr, cc = 0, 0
    while True:
        if count == N * M:
            break
        if difference == 26:
            difference = 0
        grid[cr][cc] = get_next_alphabet(initial_alphabet, difference)
        if validate_range(cr + dr[direction], cc + dc[direction]):
            pass
        else:
            direction = (direction + 1) % 4
        cr, cc = cr + dr[direction], cc + dc[direction]
        count += 1
        difference += 1
    print_grid(grid)

# 구현부
N, M = map(int, input().split())
grid = [[0 for _ in range(M)] for _ in range(N)]
solve()
