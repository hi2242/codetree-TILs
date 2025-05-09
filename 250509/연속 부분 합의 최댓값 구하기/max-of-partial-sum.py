# [0] 기본 정보
# N개의 정수
# 연속한 부분 수열 합의 최대 값
# 최소 한 개 이상의 원소

MIN_ANS = -1

def solve():
    for i in range(1, N):
        dp[i] = max(dp[i - 1], 0) + arr[i]

# 입력
# N(원소의 개수)
# 집합 정보
# 1 <= N <= 100000
# -1000 <= 정수 <= 1000
N = int(input())
arr = list(map(int, input().split()))

dp = [MIN_ANS for _ in range(N)]
dp[0] = arr[0]

# 출력
# 연속한 부분 수열 합의 최대 값
solve()
print(max(dp))