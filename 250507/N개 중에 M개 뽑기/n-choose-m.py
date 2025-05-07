# [0] 기본 조건
# 숫자(1 ~ N) M개 뽑기

# [1] 순서쌍 뽑기
# combination
# def solve(a):
#     # 종료 조건
#     if a == M + 1:
#         print(*result)
#         return

#     # 조합
#     for i in range(1, N + 1):
#         if a <= 1 or i not in result and i > result[-1]:
#             result.append(i)
#             solve(a + 1)
#             result.pop()

# 시간 복잡도를 줄이는 방식
def solve(cnt, last_num):
    # 종료 조건
    if cnt == M:
        print(*result)
        return

    # Cutting
    if N - last_num < M - cnt:
        return

    for i in range(last_num + 1, N + 1):
        result.append(i)
        solve(cnt + 1, i)
        result.pop()

# 입력
# N(숫자), M(개수)
# 1 <= M <= N <= 10
N, M = map(int, input().split())
result = []

# 출력
# 조합
# solve(1)

for i in range(1, N + 1):
    result.append(i)
    solve(1, i)
    result.pop()