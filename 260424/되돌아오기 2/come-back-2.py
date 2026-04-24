import sys

input = sys.stdin.readline

# 선언부
def solve(cmd: str):
    head, time = 0, 0
    result = -1
    for c in cmd:
        if c == 'R':
            head = (head + 1) % 4
        elif c == 'L':
            head = (head - 1) % 4
        else:
            curr_pos[0] += dx[head]
            curr_pos[1] += dy[head]
        time += 1
        if curr_pos == [0, 0]:
            result = time
            break
    print(result)

# 구현부
command = input().rstrip()
curr_pos = [0, 0]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
solve(command)
