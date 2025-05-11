# [0] 기본 조건
# N * N 격자 (0, 1, 2, 3)
# 사람 H명
# 비를 피할 M개 공간
from collections import deque

# [1] 이동
# 사람마다 가장 가까운 비를 피할 공간까지의 거리
# 0은 이동 가능, 1은 이동 불가, 2는 사람, 3은 비를 피할 공간
# 한 칸 움직일때마다 1초 소요
# 벽 빼고는 상하좌우로 이동 가능
def print_grid(array):
    for row in array:
        print(*row)
    print()

def find():
    for r in range(N):
        for c in range(N):
            if grid[r][c] == 2:
                human.append((r, c))

def solve(sr, sc):
    visited = [[0 for _ in range(N)] for _ in range(N)]
    # 상(0), 하(1), 좌(2), 우(3)
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    d = deque()
    d.append((sr, sc))
    visited[sr][sc] = 1
    count = 0
    
    while d:
        cr, cc = d.popleft()
        count += 1
        for i in range(4):
            nr, nc = cr + dr[i], cc + dc[i]

            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0 and grid[nr][nc] != 1:
                d.append((nr, nc))
                visited[nr][nc] = 1
                if grid[nr][nc] == 3:
                    return count

    return -1



# 입력
# N(격자 크기), H(사람의 수), M(비를 피할 공간의 수)
# 격자 정보
# 2 <= N <= 100
# 1 <= H, M <= N * N
# 0 <= 주어지는 숫자 <= 3
N, H, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
human = []
result = [[0 for _ in range(N)] for _ in range(N)]

# 출력
# 변경된 격자 정보
# (사람이 없던 칸 -> 0)
# (사람이 있던 칸 -> 비를 피할 공간까지의 최소 시간)
# (절대 비를 피할 수 없는 사람 -> -1)
find()

for r, c in human:
    distance = solve(r, c)
    result[r][c] = distance

print_grid(result)