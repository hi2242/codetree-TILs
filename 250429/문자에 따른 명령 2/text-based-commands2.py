# (0, 0) 북쪽을 향함
# N개의 명령에 따라 N번 움직임
# L : 왼쪽으로 90도
# R : 오른쪽으로 90도
# F : 앞으로 한 칸 이동
# 1 <= 명령의 길이 <= 100000
# 입력 : L, R, F로만 이루어진 문자열
command = input()

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def solve():
    nx = ny = 0
    dir_num = 0

    for i in range(len(command)):
        if command[i] == "L":
            dir_num = (dir_num - 1) % 4

        elif command[i] == "R":
            dir_num = (dir_num + 1) % 4

        else:
            nx += dx[dir_num]
            ny += dy[dir_num]

    return nx, ny

# 최종 위치 출력
print(*solve())
