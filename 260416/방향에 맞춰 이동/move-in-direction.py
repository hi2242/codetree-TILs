import sys

input = sys.stdin.readline

# 선언부
def move(direction: int, distance: int):
    pos[0] += dx[direction] * distance
    pos[1] += dy[direction] * distance

# 구현부
N = int(input())
pos = [0, 0]
dx, dy = [-1, 0, 0, 1], [0, -1, 1, 0]
for _ in range(N):
    direction, distance = input().rstrip().split()
    direction = (
        0 if direction == 'W' else 
        (1 if direction == 'S' else
        (2 if direction == 'N' else 3)))
    move(direction, int(distance))
print(*pos)
