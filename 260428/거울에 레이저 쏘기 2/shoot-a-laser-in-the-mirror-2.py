import sys

input = sys.stdin.readline

# 선언부
def get_start_point(start: int) -> list[int]:
    return (
        [0, start - 1, 0] if (start - 1) // N == 0 else 
        [start - N - 1, N - 1, 1] if (start - 1) // N == 1 else
        [N - 1, 3 * N - start, 2] if (start - 1) // N == 2 else
        [4 * N - start, 0, 3]
        )
def validate(r: int, c: int) -> bool:
    return 0 <= r < N and 0 <= c < N

def next_point(mirror: int, direction: int) -> int:
    nd = direction
    if mirror == 1:
        nd = (
            3 if nd == 0 else
            0 if nd == 3 else
            1 if nd == 2 else
            2)
    else:
        nd = (
            1 if nd == 0 else
            0 if nd == 1 else
            3 if nd == 2 else
            2)
    return nd

def solve(start: int):
    count = 0
    cr, cc, direction = get_start_point(start)
    dr, dc = [1, 0, -1, 0], [0, -1, 0, 1]
    while True:
        if not validate(cr, cc):
            print(count)
            break
        direction = next_point(grid[cr][cc], direction)
        cr, cc = cr + dr[direction], cc + dc[direction]
        count += 1

# 구현부
N = int(input())
grid = [[0 for _ in range(N)] for _ in range(N)]
for r in range(N):
    line = input().rstrip()
    for c in range(len(line)):
        grid[r][c] = 1 if line[c] == '\\' else 2
start = int(input())
solve(start)
