# N * M 크기의 직사각형
# "A" ~ "Z"까지 달팽이 모양으로 채우기
# "Z" 이후엔 다시 "A"부터

# [0] 알파벳 ASCII CODE
# A(65) ~ Z(90)
# ord : 알파벳 -> 정수
# chr : 정수 -> 알파벳

# [1] 알파벳 순환
# Z(90)에서 91이 된다면 다시 65가 되도록 한다.
# 65 + (k % 36)

# 입력
# N(행), M(열)
# 1 <= N, M <= 100
N, M = map(int, input().split())
grid = [[0 for _ in range(M)] for _ in range(N)]

# 우(0), 하(1), 좌(2), 상(3)
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def print_grid(array):
    for row in array:
        print(*row)

def rotation(d):
    return (d + 1) % 4

def solve():
    alpha_num = 1
    dir_num = cr = cc = 0
    k = 1
    grid[0][0] = "A"

    while k < N * M:
        nr, nc = cr + dr[dir_num], cc + dc[dir_num]
        
        if 0 <= nr < N and 0 <= nc < M and grid[nr][nc] == 0:
            grid[nr][nc] = chr(65 + (alpha_num % 36))
            cr, cc = nr, nc
            alpha_num += 1
            k += 1

        else:
            dir_num = rotation(dir_num)


# 출력
# 완성된 N * M 사각형
solve()
print_grid(grid)