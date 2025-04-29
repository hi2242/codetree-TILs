# 0, 1로 이루어진 N * N 격자
# 상하좌우 인접한 칸 중 숫자 1이 적혀 있는 칸 수가 3개 이상이면 카운트
# 단, 격자 벗어나는 경우는 숫자 1이 없다고 생각
# 1 <= N <= 100

# 입력 : 첫 번째 줄 N
# 두 번째 줄부터 N줄 동안 격자 정보

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

# 상(2), 하(0), 좌(3), 우(1)
# dx = [0, 1, 0, -1]
# dy = [1, 0, -1, 0]

# def solve():
#     count = 0
#     temp = 0
#     for i in range(N):
#         for j in range(N):
#             for dr, dc in zip(dy, dx):
#                 nx, ny = i + dr, j + dc

#                 if 0 <= nx < N and 0 <= ny < N and grid[nx][ny] == 1:
#                     temp += 1

#             if temp >= 3:
#                 count += 1
#             temp = 0

#     return count

# 상하좌우
dir_r = [-1, 1, 0, 0]
dir_c = [0, 0, -1, 1]

def solve():
    count = 0
    temp = 0
    for cr in range(N):
        for cc in range(N):
            for dr, dc in zip(dir_r, dir_c):
                nr, nc = cr + dr, cc + dc

                if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] == 1:
                    temp += 1

            if temp >= 3:
                count += 1
            temp = 0

    return count

# 출력 : 카운트된 칸 수
print(solve())