# [0] 기본 조건
# N개의 동전
# 금액 M을 맞추기 위한 최소 동전 수
# 같은 동전 중복 가능
def init():
    for elem in coin:
        dp[elem] = 1

def solve():
    for i in range(1, M + 1):
        for j in coin:
            if i - j > 0:
                dp[i] = min(dp[i - j] + 1, dp[i])

    return dp[M]

# 입력
# N(동전 수), M(금액)
# 동전 종류
# 1 <= N <= 100
# 1 <= M <= 10000
# 1 <= 동전의 금액 <= 10000
N, M = map(int, input().split())
coin = list(map(int, input().split()))
dp = [10001 for _ in range(10001)]

# 출력
# 최소 동전 수 (불가능하면 -1 출력)
init()
result = solve()
if result != 10001:
    print(result)
else:
    print(-1)