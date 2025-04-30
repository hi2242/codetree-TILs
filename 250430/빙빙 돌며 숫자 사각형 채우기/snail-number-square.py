# [0] 문제 기본 조건
# N * M 크기의 직사각형
# 숫자 1부터 순서대로 증가시키며 달팽이 모양
# 달팽이 모양 : 회전형

# [1] 벽을 만나는 경우
# 벽을 만나면 시계 방향으로 90도 회전

# [2] 칸에 이미 숫자가 있는 경우
# 숫자가 이미 있다면 (방문을 했다면) 시계 방향으로 90도 회전

# 입력
# N(행), M(열)
# 1 <= N, M <= 100
N, M = map(int, input().split())
grid = [[0 for _ in range(M)] for _ in range(N)]

# 우(0) 하(1) 좌(2) 상(3)
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def print_grid(array):
    for row in array:
        print(*row)

def rotation(d): 
    return (d + 1) % 4

def solve():
    dir_num = cr = cc = 0
    curr_num = 2
    
    grid[0][0] = 1
    k = 1

    while k < N * M:
        nr, nc = cr + dr[dir_num], cc + dc[dir_num]
        if 0 <= nr < N and 0 <= nc < M and grid[nr][nc] == 0:
            grid[nr][nc] = curr_num
            cr, cc = nr, nc
            curr_num += 1
            k += 1

        else:
            dir_num = rotation(dir_num)


grid = [[0 for _ in range(M)] for _ in range(N)]

# 출력
# 결과 격자
solve()
print_grid(grid)