# [0] 기본 정보
# N * N 격자
# N개의 칸 색칠

# [1] 색칠하기
# 각행, 각열에 칠해진 칸은 1칸
# 색칠된 칸의 합 중 최댓값
def solve(cnt, row_num):
    global count
    # 종료 조건
    if cnt == N:
        count = max(count, sum(result))
        return

    for c in list(set(std) - set(col_num)):
        result.append(grid[row_num][c])
        col_num.append(c)
        solve(cnt + 1, (row_num + 1) % N)
        result.pop()
        col_num.remove(c)

# 입력
# N(격자 크기)
# 격자 정보
# 1 <= N <= 10
# 1 <= 주어지는 정수 <= 10000
N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
result = []
col_num = []
std = [i for i in range(N)]
count = 0

# 출력
# 최댓값
solve(0, 0)
print(count)