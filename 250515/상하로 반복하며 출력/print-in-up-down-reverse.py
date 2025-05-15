N = int(input())

grid = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    if i % 2 == 0:
        for j in range(N):
            grid[j][i] = j + 1

    else:
        for j in range(N - 1, -1, -1):
            grid[j][i] = N - j


for row in grid:
    print("".join(map(str, row)))