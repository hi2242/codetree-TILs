import sys

input = sys.stdin.readline

# 선언부
def solve():
    result = 0
    for r in range(N):
        for c in range(N - 2):
            count = 0
            for i in range(3):
                if grid[r][c + i] == 1:
                    count += 1
            result = max(result, count)
    print(result)

# 구현부
N = int(input())
grid = []
for _ in range(N):
    grid.append(list(map(int, input().split())))
solve()
