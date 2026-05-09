import sys

input = sys.stdin.readline

# 선언부
def check(r: int, c: int, i: int) -> bool:
    return 0 <= r + 2 * dr[i] < N and 0 <= c + 2 * dc[i] < M

def solve():
    result = 0
    for r in range(N):
        for c in range(M):
            for i in range(8):
                if check(r, c, i) and grid[r][c] == 'L' and grid[r + dr[i]][c + dc[i]] == 'E' and grid[r + 2 * dr[i]][c + 2 * dc[i]] == 'E':
                    result += 1
    print(result)

# 구현부
N, M = map(int, input().split())
grid = [list(input().rstrip()) for _ in range(N)]
dr, dc = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]
solve()
