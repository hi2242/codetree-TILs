import sys

input = sys.stdin.readline

# 선언부
def move(dir: str, dis: int):
    global time
    for _ in range(dis):
        time += 1
        curr_pos[0] += dx[head[dir]]
        curr_pos[1] += dy[head[dir]]
        if curr_pos == [0, 0]:
            return True
    return False

# 구현부
N = int(input())
curr_pos = [0, 0]
time = 0
result = -1
dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]
head = {
    'N': 0,
    'S': 1,
    'W': 2,
    'E': 3
}
for _ in range(N):
    line = input().rstrip().split()
    direction, distance = line[0], int(line[1])
    if move(direction, distance):
        result = time
        break
print(result)
