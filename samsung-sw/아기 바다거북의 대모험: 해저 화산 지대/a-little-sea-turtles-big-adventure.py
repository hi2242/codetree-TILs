from collections import deque

# 입력부
N, M, K = map(int, input().split())
area_info_grid = [list(map(int, input().split())) for _ in range(N)]
turtles = []
volcanoes = []
for _ in range(M):
    r, c = map(int, input().split())
    turtles.append([r, c, 1])

for _ in range(K):
    r, c, p = map(int, input().split())
    volcanoes.append([r, c, p, 1])


# 선언부
# 우 -> 하 -> 좌 -> 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

DIRECTIONS_COUNT = 4

# 거북이 관련 상태
TURTLE_ALIVE = 1
TURTLE_FINISHED = 2
TURTLE_ROCK = 3
TURTLE_ALREADY_CHECKED = 4

# area_info_grid에 작성되는 상태
AREA_EMPTY = 0
AREA_FLOWER = 1
AREA_TURTLE = 2
AREA_ROCK = 3
AREA_VOLCANO = 4

INF = float('inf')

temp_grid = [[0 for _ in range(N)] for _ in range(N)]
erosion_list = []
pressure_list = [0 for _ in range(K)]
arrival_list = [-1 for _ in range(M)]

# 함수 선언부
def print_grid(grid):
    for row in grid:
        print(*row)
    print()

def turtles_move():
    for i in range(len(turtles)):
        pd, pv = -1, INF
        r, c, s = turtles[i]
        if is_finish(r, c) or s >= TURTLE_FINISHED :
            continue
        for j in range(DIRECTIONS_COUNT):
            nr, nc = r + dr[j], c + dc[j]
            if is_valid(nr, nc) and (area_info_grid[nr][nc] == AREA_EMPTY or area_info_grid[nr][nc] == AREA_VOLCANO):
                curr_v = find_path(r, c, nr, nc)
                if curr_v != -1 and pv > curr_v:
                    pd, pv = j, curr_v
        if pd != -1:
            turtles[i][0] = r + dr[pd]
            turtles[i][1] = c + dc[pd]

            area_info_grid[r][c] = AREA_VOLCANO if area_info_grid[r][c] == (AREA_TURTLE + AREA_VOLCANO) else AREA_EMPTY
            
            if not is_finish(r + dr[pd], c + dc[pd]):
                area_info_grid[r + dr[pd]][c + dc[pd]] = (AREA_TURTLE + AREA_VOLCANO) if area_info_grid[r + dr[pd]][c + dc[pd]] == AREA_VOLCANO else AREA_TURTLE
            else:
                if turtles[i][2] != TURTLE_ALREADY_CHECKED:
                    turtles[i][2] = TURTLE_FINISHED

def is_finish(r, c):
    return r == N - 1 and c == N - 1

def is_valid(r, c):
    return 0 <= r < N and 0 <= c < N

def find_path(r, c, sr, sc):
    d = deque()
    d.append((sr, sc, 1))
    visited = [[0 for _ in range(N)] for _ in range(N)]
    visited[r][c] = 1
    visited[sr][sc] = 1
    while d:
        cr, cc, cv = d.popleft()
        if is_finish(cr, cc):
            return cv
        for i in range(DIRECTIONS_COUNT):
            nr, nc = cr + dr[i], cc + dc[i]
            if is_valid(nr, nc) and visited[nr][nc] == 0 and (area_info_grid[nr][nc] == AREA_EMPTY or area_info_grid[nr][nc] == AREA_VOLCANO):
                d.append((nr, nc, cv + 1))
                visited[nr][nc] = 1
    
    return -1

def check_temp():
    for i in range(len(volcanoes)):
        r, c, p, e = volcanoes[i]
        if e and pressure_list[i] + temp_grid[r][c] >= p:
            erosion(r, c, p)
            volcanoes[i][3] = 0
            erosion_list.append((i, r, c, p))

def erosion(r, c, p):
    d = deque()
    d.append((r, c, p))
    temp_grid[r][c] += p
    visited = [[0 for _ in range(N)] for _ in range(N)]
    visited[r][c] = 1
    while d:
        cr, cc, cp = d.popleft()
        for i in range(DIRECTIONS_COUNT):
            nr, nc = cr + dr[i], cc + dc[i]
            if is_valid(nr, nc) and visited[nr][nc] == 0 and area_info_grid[nr][nc] != AREA_FLOWER:
                if cp // 2 == 0:
                    continue
                temp_grid[nr][nc] += cp // 2
                d.append((nr, nc, cp // 2))
                visited[nr][nc] = 1

def volcano_reset():
    global erosion_list
    for i in range(len(volcanoes)):
        volcanoes[i][3] = 1

    for k in range(len(erosion_list)):
        i, r, c, p = erosion_list[k]
        pressure_list[i] = 0
    erosion_list = []

def turtle_to_rock():
    for i in range(len(turtles)):
        r, c, s = turtles[i]
        if temp_grid[r][c] >= 20 and turtles[i][2] == TURTLE_ALIVE:
            area_info_grid[r][c] = (AREA_VOLCANO + AREA_ROCK) if area_info_grid[r][c] == (AREA_VOLCANO + AREA_TURTLE) else AREA_ROCK
            turtles[i][2] = TURTLE_ROCK

def temp_reset():
    for r in range(N):
        for c in range(N):
            temp_grid[r][c] = 0

def check_turtles(turn):
    for i in range(len(turtles)):
        r, c, s = turtles[i]
        if is_finish(r, c) and s == TURTLE_FINISHED:
            turtles[i][2] = TURTLE_ALREADY_CHECKED
            arrival_list[i] = turn

def update_pressure():
    for i in range(len(pressure_list)):
        pressure_list[i] += 10

def env_reset():
    volcano_reset()
    turtle_to_rock()
    temp_reset()

def init():
    for i in range(len(turtles)):
        r, c, s = turtles[i]
        area_info_grid[r][c] = AREA_TURTLE
    for i in range(len(volcanoes)):
        r, c, p, e = volcanoes[i]
        area_info_grid[r][c] = AREA_VOLCANO

def solve():
    init()
    for i in range(1, 101):
        turtles_move()
        update_pressure()
        while True:
            prev = len(erosion_list)
            check_temp()
            if prev == len(erosion_list):
                break
        check_turtles(i)
        env_reset()
    print(*arrival_list, sep = '\n')

# 구현부
solve()