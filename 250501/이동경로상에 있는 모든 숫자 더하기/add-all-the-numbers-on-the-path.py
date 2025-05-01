# [0] 문제 정보
# N * N 정사각형 격자
# (N // 2, N // 2)에서 북쪽을 향함
# T개의 명령 (L or R or F)
# L : 왼쪽으로 90도 회전
# R : 오른쪽으로 90도 회전
# F : 앞으로 이동
# 시작위치 포함해서 방문한 칸에 적혀있는 수를 누적
# 격자 범위를 벗어난 명령은 무시

# [1] 방향 회전
# L이면 CCW R이면 CW으로 회전한다.
# L : (d - 1 + 4) % 4
# R : (d + 1) % 4

# 입력
# N(격자 크기), T(명령의 개수)
# 명령
# 격자 정보
# 3 <= N <= 99
# 1 <= T <= 100000
# 1 <= 격자 안의 수 <= 9
N, T = map(int, input().split())
command = input()
grid = [list(map(int, input().split())) for _ in range(N)]

# 우(0), 하(1), 좌(2), 상(3)

def rotation(d, com):
    if com == "L":
        return (d - 1 + 4) % 4

    elif com == "R":
        return (d + 1) % 4

    else:
        return d

def solve():
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    dir_num = 3
    cr = cc = N // 2
    result = grid[cr][cc]

    for i in range(T):
        if command[i] != "F":
            dir_num = rotation(dir_num, command[i])

        elif command[i] == "F":
            nr, nc = cr + dr[dir_num], cc + dc[dir_num]

            if 0 <= nr < N and 0 <= nc < N:
                result += grid[nr][nc]
                cr, cc = nr, nc

            else:
                continue

    return result

# 출력
# 누적 값
print(solve())