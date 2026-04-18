import sys

input = sys.stdin.readline

# 선언부
def verify(a: int, b: int):
    return 0 <= a < N and 0 <= b < N

def check(r: int, c: int):
    count = 0
    for i in range(4):
        if verify(r + dr[i], c + dc[i]) and grid[r + dr[i]][c + dc[i]] == 1:
            count += 1
    return count >= 3

def solve():
    result = 0
    for r in range(N):
        for c in range(N):
            if check(r, c):
                result += 1
    print(result)

# 구현부
N = int(input())
grid = []
dr, dc = [0, 0, -1, 1], [-1, 1, 0, 0]
for _ in range(N):
    row = list(map(int, input().split()))
    grid.append(row)
solve()
