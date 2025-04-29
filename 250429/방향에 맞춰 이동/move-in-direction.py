n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Please write your code here.

# (0, 0)에서 시작하여 총 N번 이동
# 첫 번째 줄에 최종 위치 x, y를 공백을 두고 출력

# W(서) = (0, -1), S(남) = (1, 0), N(북) = (-1, 0), E(동) = (0, 1)
# 1 <= N <= 100
# 1 <= 한 번에 움직이는 거리 <= 10

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

dir_num = ["W", "S", "N", "E"]

dir_x = dict(zip(dir_num, dx))
dir_y = dict(zip(dir_num, dy))

def solve():
    nx = ny = 0
    for i in range(n):
        nx, ny = nx + (dir_x[dir[i]] * dist[i]), ny + (dir_y[dir[i]] * dist[i])

    return nx, ny

print(*solve())