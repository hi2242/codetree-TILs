# [0] 기본 조건
# N * N 격자
# 같은 마을 : 상하좌우 인접한 곳
from collections import deque
def solve(sr, sc):
    if not grid[sr][sc] or visited[sr][sc]:
        return

    tr, tc = sr, sc
    
    # 상(0), 하(1), 좌(2), 우(3)
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    d = deque()
    d.append((sr, sc))
    visited[sr][sc] = 1
    count = 1

    while d:
        cr, cc = d.popleft()

        for i in range(4):
            nr, nc = cr + dr[i], cc + dc[i]

            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0 and grid[nr][nc] == 1:
                count += 1
                visited[nr][nc] = count
                tr, tc = nr, nc
                d.append((nr, nc))

    result.append(visited[tr][tc])


# 입력
# N(격자의 크기)
# 격자 정보
# 5 <= N <= 25
N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]
result = []

# 출력
# 총 마을의 개수
# 마을 사람의 수 (오름차순)
for r in range(N):
    for c in range(N):
        solve(r, c)

print(len(result))
print(*sorted(result), sep = "\n")