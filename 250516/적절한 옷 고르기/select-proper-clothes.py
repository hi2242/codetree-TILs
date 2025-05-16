# [0] 기본 정보
# N개의 옷 중 M일 동안 입을 옷 정하기
# 만족도의 합 최대화

# [1] 옷 입기
# 각각의 옷은 입을 수 있는 기간이 존재
# M일 안에 같은 옷을 여러 번 입어도 됨
# 하루에 정확히 하나의 옷만 입음

# [2] 만족도 계산
# 만족도 : 인접한 날짜에 입은 옷의 화려함의 차이를 모두 더함
def init():
    for i in range(N):
        if grid[i][0] == 1:
            dp[0][i] = 0

def solve():
    for i in range(1, M):
        for j in range(N):
            if grid[j][0] - 1 <= i <= grid[j][1] - 1:
                for k in range(N):
                    if grid[k][0] <= i <= grid[k][1]:
                        dp[i][j] = max(dp[i][j], dp[i - 1][k] + abs(grid[j][2] - grid[k][2]))

# 입력
# N(옷 개수), M(날짜)
# s(옷을 입을 수 있는 시작 날짜), e(옷을 입을 수 있는 마지막 날짜), v(옷의 화려함)
# 1 <= N <= 200
# 2 <= M <= 200
# 1 <= s <= e <= M
# 1 <= v <= 1000
# 단, 각 날짜마다 입을 수 있는 옷이 최소한 하나는 존재
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
dp = [[-1 for _ in range(N)] for _ in range(M)]

# 출력
# 최대 만족도
init()
solve()
print(max(dp[M - 1]))