grid = [list(map(int, input().split())) for _ in range(4)]

count = 0
for i in range(4):
    for j in range(4):
        if grid[i][j] % 5 == 0:
            count += 1

print(count)