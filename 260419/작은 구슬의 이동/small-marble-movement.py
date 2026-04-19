import sys

input = sys.stdin.readline

# 선언부
def direction(d: str):
    di = -1
    if d == 'U':
        di = 0
    elif d == 'D':
        di = 1
    elif d == 'L':
        di = 2
    elif d == 'R':
        di = 3
    return di

def check_direction(r: int, c: int, d: str):
    new_direction = d
    if R == 1 and new_direction == 'U':
        new_direction = 'D'
    elif R == N and new_direction == 'D':
        new_direction = 'U'
    elif C == 1 and new_direction == 'L':
        new_direction = 'R'
    elif C == N and new_direction == 'R':
        new_direction = 'L'
    return new_direction

def move():
    global R, C, D
    new_D = check_direction(R, C, D)
    if D != new_D:
        D = new_D
        return
    di = direction(D)
    R += dr[di]
    C += dc[di]

# 구현부
N, T = map(int, input().split())
line = input().rstrip().split()
R, C, D = int(line[0]), int(line[1]), line[2]
grid = [[0 for _ in range(N)] for _ in range(N)]
dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]
curr_pos = [R, C]
for _ in range(T):
    move()
print(R, C)
