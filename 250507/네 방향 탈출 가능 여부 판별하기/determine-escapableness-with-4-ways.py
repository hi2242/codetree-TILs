# [0] 기본 정보
# N * M 격자
# 출발(0, 0), 도착(N - 1, M - 1)
# 뱁 있음(0), 없음(1)
from collections import deque

# [1] 이동
# 뱀이 없는 상(-1, 0), 하(1, 0), 좌(0, -1), 우(0, 1)
def solve(sr, sc):
    # 상(0), 하(1), 좌(2), 우(3)
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    d = deque()
    d.append((sr, sc))
    visited[0][0] = 1

    while d:
        cr, cc = d.popleft()

        for i in range(4):
            nr, nc = cr + dr[i], cc + dc[i]

            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0 and grid[nr][nc] == 1:
                visited[nr][nc] = 1
                d.append((nr, nc))



# 입력
# N(행), M(열)
# 격자 정보
# 2 <= N, M <= 100
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]




# 출력
# 탈출 가능(1), 불가능(0) 여부 출력
solve(0, 0)
print(visited[N - 1][M - 1])