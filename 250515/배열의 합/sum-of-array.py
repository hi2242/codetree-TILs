grid = [list(map(int, input().split())) for _ in range(4)]

for row in grid:
    print(sum(row))