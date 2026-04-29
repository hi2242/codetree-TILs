import sys

input = sys.stdin.readline

# 선언부
def solve():
    position = [0, 0]
    current_color = grid[0][0]
    result = 0
    if grid[0][0] == grid[R - 1][C - 1]:
        print(result)
        return
    for i in range(1, R - 1):
        for j in range(1, C - 1):
            if grid[i][j] != current_color:
                for k in range(i + 1, R - 1):
                    for l in range(j + 1, C - 1):
                        if grid[k][l] == current_color:
                            result += 1
    print(result)

# 구현부
R, C = map(int, input().split())
grid = []
for _ in range(R):
    grid.append(input().rstrip().split())
solve()
