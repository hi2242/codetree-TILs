import sys

input = sys.stdin.readline

# 선언부
def solve():
    global head
    for command in line:
        if command == 'L':
            head = (head - 1) % 4
        elif command == 'R':
            head = (head + 1) % 4
        else:
            position[0] += dx[head]
            position[1] += dy[head]
    print(*position)

# 구현부
line = input().rstrip()
# 북 동 남 서
head, position = 0, [0, 0]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
solve()
