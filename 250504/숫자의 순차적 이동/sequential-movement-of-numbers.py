# [0] 기본 정보
# N * N 격자 (1 ~ N * N)
# M번에 걸쳐 수들을 이동

def print_grid(array):
    for row in array:
        print(*row)

# [1] 수들의 이동
# 1부터 N * N까지 순서대로 (다 돌려야 한 턴)
# 인접한 여덟방향에서 가장 큰 수와 가운데 수 교환
def find(idx):
    for r in range(N):
        if idx in grid[r]:
            return r, grid[r].index(idx)

def compare(r, c):
    # 상(0), 우상(1), 우(2), 우하(3), 하(4), 좌하(5), 좌(6), 좌상(7)
    dr = [-1, -1, 0, 1, 1, 1, 0, -1]
    dc = [0, 1, 1, 1, 0, -1, -1 ,-1]
    temp = 0

    for i in range(8):
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < N and 0 <= nc < N and temp < grid[nr][nc]:
            temp = grid[nr][nc]
            tr, tc = nr, nc

    return temp, tr, tc

def move():
    global grid
    for i in range(1, N * N + 1):
        cr, cc = find(i)
        temp, nr, nc = compare(cr, cc)
        grid[cr][cc], grid[nr][nc] = temp, i

def solve():
    for _ in range(M):
        move()

# 입력
# N(격자의 크기), M(턴의 수)
# 격자 정보
# 숫자 중복 없음
# 2 <= N <= 20
# 1 <= M <= 100
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

# 출력
# 최종 격자
solve()
print_grid(grid)