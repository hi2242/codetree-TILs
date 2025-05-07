# [0] 기본 정보
# N * M 격자

# [1] 이동
# 아래(1, 0), 오른쪽(0, 1)으로만 이동
# 뱀이 있으면 이동 불가
def solve(cr, cc):
    if visited[N - 1][M - 1] == 1:
        return

    for i in range(2):
        nr, nc = cr + dr[i], cc + dc[i]
        
        if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0 and grid[nr][nc] == 1:
            visited[nr][nc] = 1
            solve(nr, nc)

# 입력
# N(행), M(열)
# 격자 정보 (시작과 끝엔 뱀이 없음)
# 2 <= N, M <= 100
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]

dr = [1, 0]
dc = [0, 1]
visited[0][0] = 1

# 출력
# 탈출 가능 여부
solve(0, 0)

print(visited[N - 1][M - 1])