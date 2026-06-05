import sys

input = sys.stdin.readline

# 선언부
INF = float('inf')

def solve():
    result = "No"
    for i in range(N):
        max_x1, min_x2 = 0, INF
        for j in range(N):
            if i == j:
                continue
            max_x1 = max(max_x1, lines[j][0])
            min_x2 = min(min_x2, lines[j][1])
        if max_x1 <= min_x2:
            result = "Yes"
    print(result)

# 구현부
N = int(input())
lines = [list(map(int, input().split())) for _ in range(N)]
solve()
