# [0] 기본 조건
# 숫자(1 ~ K) 고르기 N번 반복

# [1] 순서쌍 고르기
# 서로 다른 순서쌍 (연속하여 숫자가 3번 이상 나오는 경우 제외)
def solve(a):
    # 종료 조건
    if a == N + 1:
        print(*result)
        return
    # 순서쌍 고르기
    for i in range(1, K + 1):
        if a < 3 or result[-2:] != [i, i]:
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
# 순서쌍 결과
solve(1)