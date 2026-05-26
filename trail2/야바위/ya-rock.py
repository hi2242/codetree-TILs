import sys

input = sys.stdin.readline

# 선언부
def solve():
    result = 0
    for i in range(1, 4):
        cups = [0 for _ in range(4)]
        cups[i] = 1
        temp = 0
        for j in range(N):
            a, b, c = grid[j]
            cups[a], cups[b] = cups[b], cups[a]
            if cups[c] == 1:
                temp += 1
        result = max(result, temp)
    print(result)

# 구현부
N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
solve()
