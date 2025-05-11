# [0] 기본 조건
# N * N 격자 (0, 1)
# K개의 시작점
from collections import deque

# [1] 이동
# 인접한 상하좌우
# 0은 이동 가능, 1은 이동 불가
def add_elem(r, c, arr):
    if (r, c) not in arr:
        arr.append((r, c))

def solve(sr, sc):
    # 상(0), 하(1), 좌(2), 우(3)
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    d = deque()
    d.append((sr, sc))
    visited[sr][sc] = 1
    add_elem(sr, sc, result)

    while d:
        cr, cc = d.popleft()
        
        for i in range(4):
            nr, nc = cr + dr[i], cc + dc[i]
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0 and grid[nr][nc] == 0:
                d.append((nr, nc))
                visited[nr][nc] = 1

                add_elem(nr, nc, result)


# 입력
# N(격자 크기), K(시작점의 수)
# 격자 정보
# 시작점 정보 (시작점 정보는 0, 시작점은 중복되지 않음)
# 1 <= N <= 100
# 1 <= K <= N * N
# 1 <= r, c, <= N
N, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
start = [list(map(int, input().split())) for _ in range(K)]
visited = [[0 for _ in range(N)] for _ in range(N)]
result = []

# 출력
# 방문 가능한 서로 다른 칸의 수
for r, c in start:
    solve(r - 1, c - 1)
print(len(result))