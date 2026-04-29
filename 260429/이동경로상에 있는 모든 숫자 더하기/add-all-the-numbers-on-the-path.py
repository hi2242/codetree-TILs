import sys

input = sys.stdin.readline

# 선언부
def validate(r: int, c: int):
    return 0 <= r < N and 0 <= c < N

def solve():
    direction = 0
    cr = cc = N // 2
    count = grid[cr][cc]
    for c in command:
        if c == 'R':
            direction = (direction + 1) % 4
        elif c == 'L':
            direction = (direction - 1) % 4
        else:
            if validate(cr + dr[direction], cc + dc[direction]):
                cr, cc = cr + dr[direction], cc + dc[direction]
                count += grid[cr][cc]
    print(count)

# 구현부
N, T = map(int, input().split())
command = input().rstrip()
dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]
grid = []
for _ in range(N):
    grid.append(list(map(int, input().split())))
solve()
