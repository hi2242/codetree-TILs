# [0] 문제 조건
# 2 * N개 컨베이어 벨트
# T초 동안 1초에 한 칸씩
# 시계방향으로 밀기

# [1] 시계 방향 회전
# up_temp와 down_temp에 저장해뒀다가 밀고나서 배치
# def rotation(grid):
#     up_temp = grid[0][N - 1]
#     down_temp = grid[1][0]

#     t_belt = [[0 for _ in range(N)] for _ in range(2)]
    
#     for i in range(N - 1, -1, -1):

def print_grid(array):
    for row in array:
        print(*row)

def rotation():
    top_temp = belt[0][N - 1]
    down_temp = belt[1][N - 1]
    
    for i in range(N - 1, 0, -1):
        belt[0][i] = belt[0][i - 1]
        belt[1][i] = belt[1][i - 1]
        
    belt[0][0] = down_temp
    belt[1][0] = top_temp

def solve():
    for _ in range(T):
        rotation()

# 입력
# N(길이), T(시간)
# 컨베이어 벨트 상황
N, T = map(int, input().split())
belt = [list(map(int, input().split())) for _ in range(2)]

# 출력
# T초 후 컨베이어 벨트
solve()
print_grid(belt)