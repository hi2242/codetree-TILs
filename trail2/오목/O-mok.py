import sys

input = sys.stdin.readline

# 선언부
def print_grid(grid: list[list[int]]):
    for row in grid:
        print(*row)

def check_arround(color: int, r: int, c: int) -> bool:
    result = False
    # 가로
    if (
        grid[r][c - 1] == color and
        grid[r][c - 2] == color and
        grid[r][c + 1] == color and
        grid[r][c + 2] == color
    ):
        result = True
    # 세로
    if (
        grid[r - 1][c] == color and
        grid[r - 2][c] == color and
        grid[r + 1][c] == color and
        grid[r + 2][c] == color
    ):
        result = True
    # 대각
    if (
        grid[r - 1][c - 1] == color and
        grid[r - 2][c - 2] == color and
        grid[r + 1][c + 1] == color and
        grid[r + 2][c + 2] == color
    ):
        result = True
    if (
        grid[r - 1][c + 1] == color and
        grid[r - 2][c + 2] == color and
        grid[r + 1][c - 1] == color and
        grid[r + 2][c - 2] == color
    ):
        result = True
    return result

def solve():
    result = 0
    position = [0, 0]
    for r in range(2, 19):
        for c in range(2, 19):
            if grid[r][c] != 0 and check_arround(grid[r][c], r, c):
                print(grid[r][c])
                print(r + 1, c + 1)
                return
    print(result)

# 구현부
grid = [list(map(int, input().split())) for _ in range(19)]
solve()
