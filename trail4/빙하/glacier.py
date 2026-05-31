import sys
from collections import deque

input = sys.stdin.readline

# 선언부
def print_grid(grid):
    for row in grid:
        print(*row)

def init(dr, dc, visited):
    d = deque()
    for r in range(N):
        for c in range(M):
            if r == 0 or c == 0 or r == N - 1 or c == M - 1:
                d.append((r, c))
                visited[r][c] = 1
    return d

def solve():
    visited = [[0 for _ in range(M)] for _ in range(N)]
    dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]
    d = init(dr, dc, visited)
    last, time = 0, 0
    temp_d = deque()
    while d:
        cr, cc = d.popleft()
        temp = 0
        for i in range(4):
            nr, nc = cr + dr[i], cc + dc[i]
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                if grid[nr][nc]:
                    visited[nr][nc] = 1
                    temp_d.append((nr, nc))
                else:
                    visited[nr][nc] = 1
                    d.append((nr, nc))
        
        if not len(d):
            d = temp_d.copy()
            if len(temp_d):
                time += 1
                last = len(temp_d)
            temp_d = deque()
                
    print(time, last)

# 구현부
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
solve()
