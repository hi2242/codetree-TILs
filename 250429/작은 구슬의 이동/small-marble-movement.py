# N * N 격자
# 1초마다 상하좌우 중 바라보는 방향으로 한 칸 움직임
# 벽에 부딪히면 방향이 바뀌고 1초가 소모됨
# T초기 지난 후의 위치

# 입력
# 첫 번째 줄 : N(격자 크기), T(시간)
# 두 번째 줄 : R(구슬의 시작 행), C(구슬의 시작 열), D(U(상), D(하), R(우), L(좌)중 하나)
# 2 <= N <= 50
# 1 <= T <= 100
# 1 <= R, C <= N
# D = U, D, R, L

N, T = map(int, input().split())
R, C, D = input().split()

R, C = int(R), int(C)
dr = [0, 1, -1, 0]
dc = [1, 0, 0, -1]

dir_str = {
    "U" : 2,
    "D" : 1,
    "R" : 0,
    "L" : 3,
}

def solve():
    cr, cc = R, C
    dir_num = dir_str[D]

    for i in range(T):
        nr, nc = cr + dr[dir_num], cc + dc[dir_num]
        if 1 <= nr < N + 1 and 1 <= nc < N + 1:
            cr, cc = nr, nc
        else:
            dir_num = 3 - dir_num 

    return cr, cc

# 출력
# T초 후 구슬의 행 열 (공백 구분 출력)
print(*solve())