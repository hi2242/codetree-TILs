import sys

input = sys.stdin.readline

# 선언부
def paint(r: int, c: int):
    grid[r - 1][c - 1] = 1
def check(r: int, c: int):
    count = 0
    for dr, dc in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        nr, nc = r - 1 + dr, c - 1 + dc
        if 0 <= nr < N and 0 <= nc < N and grid[nr][nc]:
            count += 1
    print(1 if count == 3 else 0)
    
def solve(r: int, c: int):
    paint(r, c)
    check(r, c)

# 구현부
N, M = map(int, input().split())
grid = [[0 for _ in range(N)] for _ in range(N)]
for _ in range(M):
    r, c = map(int, input().split())
    solve(r, c)
