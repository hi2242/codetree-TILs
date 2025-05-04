# [0] 기본 조건
# N * M 격자 (0 ~ 9)
# Q번의 바람

def print_grid(array):
    for row in array:
        print(*row)
        
# [1] 바람의 특징
# 특정 행의 모든 원소들을 왼쪽 or 오른쪽으로 전부 한 칸씩 shift
def move(idx, cd):
    global grid

    if cd == "L":
        temp = grid[idx][M - 1]
        for i in range(M - 1, 0, -1):
            grid[idx][i] = grid[idx][i - 1]

        grid[idx][0] = temp

    elif cd == "R":
        temp = grid[idx][0]
        for i in range(0, M - 1):
            grid[idx][i] = grid[idx][i + 1]

        grid[idx][M - 1] = temp

# [2] 바람의 전파
# shift 이후 현재 행과 나아가려는 행을 비교했을 떄 같은 열에 같은 숫자가 있으면 전파
# 더이상 전파의 조건에 맞는게 없을 때까지 진행
def check(idx, cd):
    if cd == "UP":
        for i in range(M):
            if grid[idx][i] == grid[idx - 1][i]:
                return True

    elif cd == "DOWN":
        for i in range(M):
            if grid[idx][i] == grid[idx + 1][i]:
                return True

    return False

def change_dir(cd):
    if cd == "L":
        return "R"

    elif cd == "R":
        return "L"

def affect(idx):
    move(int(wind[idx][0]) - 1, wind[idx][1])

    new_idx = int(wind[idx][0]) - 1
    new_dir = wind[idx][1]

    while new_idx > 0 and check(new_idx, "UP"):
        new_idx -= 1
        new_dir = change_dir(new_dir)
        move(new_idx, new_dir)

    new_idx = int(wind[idx][0]) - 1
    new_dir = wind[idx][1]
    while new_idx < N - 1 and check(new_idx, "DOWN"):
        new_idx += 1
        new_dir = change_dir(new_dir)
        move(new_idx, new_dir)
        

def solve():
    for i in range(Q):
        affect(i)

# 입력
# N(행), M(열), Q(바람의 횟수)
# 격자의 상태
# r(바람이 불 행), d(바람이 불어오는 방향 'L' or 'R')
# 1 <= N <= 100
# 1 <= M <= 100
# 0 <= Q <= 100
# 1 <= r <= N
N, M, Q = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
wind = [list(input().split()) for _ in range(Q)]

# 출력
# 바람이 모두 분 이후의 격자 상태
solve()
print_grid(grid)