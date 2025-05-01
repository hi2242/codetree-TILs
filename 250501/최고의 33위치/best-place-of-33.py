# n = int(input())
# grid = [list(map(int, input().split())) for _ in range(n)]

# # Please write your code here.
# import sys

# input = sys.stdin.readline

# def solve(array):
#     result = 0
#     for i in range(n - 2):
#         for j in range(n - 2):
#             temp = 0
#             for k in range(i, i + 3):
#                 temp += array[k][j : j + 3].count(1)
#             if result < temp:
#                 result = temp

#     return result

# print(solve(grid))

# N * N 격자
# 1(동전 있음), 0(동전 없음)
# 3 * 3 격자 안에 동전의 개수가 최대가 되도록

# 입력
# N(격자의 크기)
# 격자 정보
# 3 <= N <= 20
N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

def check(tr, tc):
    count = 0
    for r in range(3):
        for c in range(3):
            if grid[tr + r][tc + c] == 1:
                count += 1

    return count

def solve():
    result = 0
    for r in range(N - 2):
        for c in range(N - 2):
            if result < check(r, c):
                result = check(r, c)

    return result

# 출력
# 최대 동전의 수
print(solve())