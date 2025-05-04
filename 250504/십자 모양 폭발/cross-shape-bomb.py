# [0] 기본 정보
# N * N 격자 (1 ~ 100)

def print_grid(array):
    for row in array:
        print(*row)

# [1] 십자 폭탄
# 특정 위치를 선택하면 십자 모양으로 폭발 (폭발한 숫자는 사라짐)
# 십자 모양의 크기는 특정 위치의 숫자에 따라 정해짐
def bomb():
    global grid
    # 상(0), 하(1), 좌(2), 우(3)
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for i in range(4):
        nr, nc = r - 1, c - 1
        for _ in range(grid[r - 1][c - 1] - 1):
            nr, nc = nr + dr[i], nc + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                grid[nr][nc] = 0
                
            else:
                break

    grid[r - 1][c - 1] = 0

# [2] 중력
# 중력에 의해 다른 숫자들이 아래로 떨어짐
def drop():
    global grid
    global new_grid
    for i in range(N):
        idx = N - 1

        # 기존 제출했던 답에서 중복되는 행동을 제거한 형태
        for j in range(N - 1, -1, -1):
            if grid[j][i]:
                new_grid[idx][i] = grid[j][i]
                idx -= 1

            # if grid[j][i] == 0:

                # for k in range(j - 1, -1, -1):
                #     if grid[k][i] != 0:
                #         grid[j][i] = grid[k][i]
                #         grid[k][i] = 0
                #         break

def solve():
    bomb()
    drop()

# 입력
# N(격자의 크기)
# 격자 정보
# r(폭탄 행), c(폭탄 열)
# 1 <= N <= 200
# 1 <= r, c <= N
N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
new_grid = [[0 for _ in range(N)] for _ in range(N)]
r, c = map(int, input().split())

# 출력
# 최종 격자 (숫자가 없으면 0으로 채움)
solve()
print_grid(new_grid)