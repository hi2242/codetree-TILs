# [0] 기본 정보
# N * N 격자 (0 or 1)
# 0(빈 칸), 1(채워진 칸)
def print_grid(array):
    for row in array:
        print(*row)

# [1] 블럭 생성
# 1 * M 크기의 블럭이 격자 위에서 떨어짐
# K ~ K + M - 1번째 열까지 공간 차지
# 다른 블럭과 맞닿거나 바닥에 닿으면 멈춤
def drop():
    status = False
    for i in range(N):
        if 1 in grid[i][K - 1:K - 1 + M]:   
            grid[i - 1][K - 1:K + M - 1] = [1 for _ in range(M)]
            break
        elif N == 1 and not grid[i][K - 1]:
            grid[i][K - 1] = 1

def solve():
    drop()

# 입력
# N(격자의 크기), M(블록의 크기), K(블록이 떨어질 위치)
# 격자 정보
# 첫 번째 행은 전부 0
# 1 <= N <= 100
# 1 <= M <= N
# 1 <= K <= N - M + 1
N, M, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

# 출력
# 최종 격자
solve()
print_grid(grid)