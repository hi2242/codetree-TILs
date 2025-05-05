# [0] 기본 정보
# 숫자(1 ~ N)를 한 번씩만 사용
def solve(a):
    # 종료 조건
    if a == N + 1:
        print(*result)
        return

    for i in range(1, N + 1):
        if visited[i]:
            continue

        result.append(i)
        visited[i] = 1

        solve(a + 1)

        result.pop()
        visited[i] = 0

# 입력
# N(숫자)
# 1 <= N <= 8
N = int(input())
result = []
visited = [0 for _ in range(N + 1)]

# 출력
# 수열
solve(1)