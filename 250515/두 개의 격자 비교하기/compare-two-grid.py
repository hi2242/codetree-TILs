N, M = map(int, input().split())

grid1 = [list(map(int, input().split())) for _ in range(N)]
grid2 = [list(map(int, input().split())) for _ in range(N)]

grid3 = [[1 for _ in range(M)] for _ in range(N)]

for i in range(N):
    for j in range(M):
        if grid1[i][j] == grid2[i][j]:
            grid3[i][j] = 0

for row in grid3:
    print(" ".join(map(str, row)))
