import sys

input = sys.stdin.readline

# 선언부
def print_extend(grid: list[int]):
    result = 0
    for i in range(201):
        for j in range(201):
            if grid[i][j] == 1:
                result += 1
    print(result)

def solve(x1: int, y1: int, x2: int, y2: int):
    for r in range(y1, y2):
        for c in range(x1, x2):
            grid[r + 100][c + 100] = 1
# 구현부
N = int(input())
grid = [[0 for _ in range(201)] for _ in range(201)]

for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    solve(x1, y1, x2, y2)
print_extend(grid)
