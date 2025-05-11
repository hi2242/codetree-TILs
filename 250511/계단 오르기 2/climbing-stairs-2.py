# [0] 기본 정보
# N층

# [1] 계단 오르기
# 한 번에 1계단 or 2계단 (1계단 오르는 것은 3번까지만)
# 단, N층까지 1계단 남으면 꼭 1계단만 오를 것

# [2] 동전 줍기
# 층에 있는 동전 줍기
def init():
    dp[0][0] = 0

    for i in range(2, N + 1, 2):
        dp[i][0] = dp[i - 2][0] + arr[i]

def in_range(a):
    return 0 <= a <= N

def solve():
    for i in range(N + 1):
        for j in range(1, min(i + 1, 4)):
            if in_range(i - 1) and in_range(i - 2) and dp[i - 1][j - 1] == -1 and dp[i - 2][j] == -1:
                continue

            if in_range(i - 1) and in_range(i - 2) and dp[i - 1][j - 1] != -1 and dp[i - 2][j] != -1:
                dp[i][j] = max(dp[i - 1][j - 1], dp[i - 2][j]) + arr[i]

            elif in_range(i - 1) and dp[i - 1][j - 1] != -1:
                dp[i][j] = max(dp[i - 1][j - 1], dp[i][j]) + arr[i]

            elif in_range(i - 2) and dp[i - 2][j] != -1:
                dp[i][j] = max(dp[i - 2][j], dp[i][j]) + arr[i]
# 입력
# N(층 수)
# 층 정보
# 2 <= N <= 1000
# 1 <= 동전의 개수 <= 1000
N = int(input())
arr = list(map(int, input().split()))
arr[0:0] = [0]
dp = [[-1 for _ in range(4)] for _ in range(N + 1)]


# 출력
# 주운 동전 개수 총합
init()
solve()
print(max(dp[N]))