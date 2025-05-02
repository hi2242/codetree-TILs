# n, m = map(int, input().split())
# grid = [list(map(int, input().split())) for _ in range(n)]

# # Please write your code here.
# # 1 이상 100이하의 숫자로만 이루어진 N * N 격자
# # 행복한 수열 = 연속하여 M개 이상의 동일한 원소가 나오는 순간이 존재하는 수열

# # **문제
# # 각 행과 각 열 총 2N개의 수열 중 행복한 수열의 개수를 출력
# import sys

# input = sys.stdin.readline

# def solve(array):
#     result = 0
#     largest = 1
#     count = 1

#     for i in range(n):
#         if largest >= m:
#             result += 1
#             largest = 1
#             count = 1

#         for j in range(n - 1):

#             if array[i][j] == array[i][j + 1]:
#                 count += 1

#             else:
#                 count = 1
                
#             if largest < count:
#                 largest = count


#     if m != 1 and largest == m:
#         result += 1

#     largest = 1

#     for i in range(n):
#         if largest >= m:
#             result += 1
#             largest = 1
#             count = 1

#         for j in range(n - 1):
#             if array[j][i] == array[j + 1][i]:
#                 count += 1

#             else:
#                 count = 1

#             if largest < count:
#                 largest = count

#     if m != 1 and largest == m:
#         result += 1

#     return result

# print(solve(grid))

# [0] 기본 조건
# N * N 격자 (1 ~ 100)
# 행복한 수열 : 연속하여 M 개 이상의 동일한 원소가 나오는 순간이 존재하는 수열
# ex) 1 2 2 (M = 2), 1 1 1 (M = 3) 등
# 총 2N개의 수열

# [1] 수열 추출
# N * N 격자에서 2N개의 수열 추출
def extract():
    t_list = []
    for r in range(N):
        t_list.append(grid[r][:])

    for c in range(N):
        temp = []
        for r in range(N):
            temp.append(grid[r][c])
        t_list.append(temp)

    return t_list


# [2] 행복한 수열 판별
# 연속하는 M개 이상의 동일한 원소 확인
def check(temp):
    count = 0
    for arr in temp:
        len_arr = 1
        for i in range(1, len(arr)):
            if arr[i - 1] == arr[i]:
                len_arr += 1

            if len_arr >= M:
                count += 1
                break

    return count

def solve():
    a_list = extract()
    
    return check(a_list)

# 입력
# N(격자의 크기), M(연속해야 하는 숫자의 수)
# 격자 정보
# 1 <= M <= N <= 100
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

# 출력
# 행복한 수열의 수
print(solve())