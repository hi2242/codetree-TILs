# [0] 기본 정보
# N * N 격자판 (1 ~ 100)
# 특정 위치 시작

# [1] 주위 비교
# 현재 위치의 숫자 < 인접 위치의 숫자 -> 이동 (상하좌우)
# 현재 위치가 인접 위치보다 크면 멈춤
def solve():
    visited = []
    # 상(0), 하(1), 좌(2), 우(3)
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    cr, cc = r - 1, c - 1
    visited.append(grid[cr][cc])

    while True:
        for i in range(4):
            nr, nc = cr + dr[i], cc + dc[i]

            if 0 <= nr < N and 0 <= nc < N and grid[cr][cc] < grid[nr][nc]:
                cr, cc = nr, nc
                visited.append(grid[nr][nc])
                break

        else:
            break

    return visited

# 입력
# N(격자의 크기), r(시작 행), c(시작 열)
# 격자의 정보
# 1 <= N <= 100
# 1 <= r, c <= N
N, r, c = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

# 출력
# 방문했던 숫자들
print(*solve())