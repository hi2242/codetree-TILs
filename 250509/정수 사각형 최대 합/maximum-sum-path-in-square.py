# [0] 기본 정보
# N * N 격자
# (1, 1)에서 시작, (N, N) 도착
# 최대 합

# [1] 이동
# 오른쪽(0, 1), 밑(1, 0)으로만 이동
def init():
    temp = grid[0][0]

    for i in range(1, N):
        temp += grid[0][i]
        dp[0][i] = temp

    temp = grid[0][0]

    for i in range(1, N):
        temp += grid[i][0]
        dp[i][0] = temp

def solve():
    for r in range(1, N):
        for c in range(1, N):
            dp[r][c] = max(dp[r][c - 1], dp[r - 1][c]) + grid[r][c]

    return dp[N - 1][N - 1]
# 입력
# N(격자 크기)
# 격자 정보
# 1 <= N <= 100
# 1 <= 행렬에 주어지는 숫자 <= 1000000
N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
dp = [[0 for _ in range(N)] for _ in range(N)]
dp[0][0] = grid[0][0]

# 출력
# 최대 합
init()
print(solve())