# [0] 기본 정보
# N번째 피보나치 수

# [1] 피보나치 수열
# 이전 두 항의 합이 그 다음 항이 되는 수열
def solve():
    dp = [0 for _ in range(N + 2)]
    dp[1] = dp[2] = 1

    for i in range(3, N + 2):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[N]

# 입력
# N(N번째 수)
# 1 <= N <= 45
N = int(input())

# 출력
# N번째 피보나치 수
print(solve())