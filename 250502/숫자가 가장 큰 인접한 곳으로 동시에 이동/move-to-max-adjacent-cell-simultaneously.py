# [0] 기본 정보
# N * N 격자판 (1 ~ 100)
# M개의 구슬 (서로 다른 위치)
def print_grid(array):
    for row in array:
        print(*row)
    print()
    
def update_grid(temp):
    for r, c in t_list:
        temp[r - 1][c - 1] += 1

    return temp

# [1] 구슬의 이동
# 인접한 값 중 가장 큰 값으로 이동 (상하좌우)
# 구슬이 움직인 후의 위치가 다르다면 충돌하지 않음
def check(tr, tc, dr, dc):
    t = 0
    for i in range(4):
        nr, nc = tr + dr[i], tc + dc[i]
        if 0 <= nr < N and 0 <= nc < N:
            if t < grid[nr][nc]:
                t = grid[nr][nc]
                dir_num = i

    return dir_num

def move(temp):
    t = 0
    # 상(0), 하(1), 좌(2), 우(3)
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    t_temp = [[0 for _ in range(N)] for _ in range(N)]

    for r in range(N):
        for c in range(N):
            if temp[r][c] == 1:
                dir_num = check(r, c, dr, dc)
                if dir_num != None:
                    t_temp[r + dr[dir_num]][c + dc[dir_num]] += 1

    return t_temp

# [2] 구슬의 삭제
# 구슬이 움직인 후의 위치가 같다면 해당 구슬들은 모두 삭제
def update(temp):
    for r in range(N):
        for c in range(N):
            if temp[r][c] != 0 and temp[r][c] != 1:
                temp[r][c] = 0

    return temp

def solve():
    t_grid = [[0 for _ in range(N)] for _ in range(N)]
    r_grid = update_grid(t_grid)
    count = 0
    # 상(0), 하(1), 좌(2), 우(3)
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for _ in range(T):
        r_grid = move(r_grid)
        r_grid = update(r_grid)


    for row in r_grid:
        if 1 in row:
            count += row.count(1)

    return count
# 입력
# N(격자의 크기), M(구슬의 개수), T(시간)
# 격자 정보
# ri(구슬의 행), ci(구슬의 열) (시작 위치는 모두 다르다)
# 2 <= N <= 20
# 1 <= M <= N * N
# 1 <= T <= 100
# 1 <= r, c <= N
N, M, T = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

t_list = []
for _ in range(M):
    ri, ci = map(int, input().split())
    t_list.append((ri, ci))

# 출력
# T초 이후 남은 구슬 수
print(solve())