import sys

input = sys.stdin.readline

# 선언부
def print_grid(grid: list[list[int]]):
    for row in grid:
        print(*row)
def validate(r: int, c: int):
    return 0 <= r < N and 0 <= c < M and grid[nr][nc] != 0

def check(r: int, c: int, head: int):
    nr, nc = r + dr[head], c + dr[head]
    new_head = -1
    if head == 0 and (nr < 0 or validate(nr, nc)):
        new_head = 3
    elif head == 1 and (nr > N - 1 or validate(nr, nc)):
        new_head = 2
    elif head == 2 and (nc < 0 or validate(nr, nc)):
        new_head = 0
    elif head == 3 and (nc > M - 1 or validate(nr, nc)):
        new_head = 1

def solve():
    current_value, current_head = 1, 0
    r, c = 0, 0
    while True:
        if current_value > N * M:
            break
        grid[r][c] = current_value
        current_value += 1
        current_head = check(r, c, current_head)
        r += dr[current_head]
        c += dc[current_head]
    
# 구현부
N, M = map(int, input().split())
grid = [[0 for _ in range(M)] for _ in range(N)]
dr, dc = [0, 0, -1, 1], [-1, 1, 0, 0]
solve()
print_grid(grid)
