# [0] 기본 조건
# 숫자(1 ~ K)고르기 N번
# 서로 다른 순서쌍

# [1] 순서쌍 고르기
# 중복 허용되게 고르기 (순열)
def solve(a):
    # 종료 조건
    if a == N + 1:
        print(*result)
        return

    for i in range(1, K + 1):
        result.append(i)
        solve(a + 1)
        result.pop()

# 입력
# K(숫자), N(횟수)
# 1 <= K <= 4
# 1 <= N <= 8
K, N = map(int, input().split())
result = []

# 출력
# 서로 다른 순서쌍
solve(1)