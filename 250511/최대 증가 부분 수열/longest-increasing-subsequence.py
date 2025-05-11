# [0] 기본 조건
# N개의 숫자
# 가장 긴 증가 부분 수열의 길이

# [1] 증가 부분 수열
# 순서대로 나열해서 만들 수 있어야 한다.
# [1, 6, 4, 3, 9, 3]에서 [1, 3, 6]은 못만들고 [1, 4, 9]는 만들 수 있다.
def solve():
    for i in range(1, N):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)

# 입력
# N(숫자 개수)
# 수열 정보
# 1 <= N <= 1000
# 1 <= 수열의 원소 <= 10000
N = int(input())
arr = list(map(int, input().split()))
dp = [1 for _ in range(N)]

# 출력
# 최장 증가 부분 수열의 길이
solve()
print(max(dp))