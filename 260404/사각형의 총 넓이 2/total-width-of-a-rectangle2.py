import sys

input = sys.stdin.readline

# 선언부
def solve(x1: int, y1: int, x2: int, y2: int):
    global extend
    for r in range(y1, y2):
        for c in range(x1, x2):
            if grid[r + 100][c + 100] == 0:
                grid[r + 100][c + 100] = 1
                extend += 1
# 구현부
N = int(input())
grid = [[0 for _ in range(201)] for _ in range(201)]
extend = 0
for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    solve(x1, y1, x2, y2)
print(extend)
