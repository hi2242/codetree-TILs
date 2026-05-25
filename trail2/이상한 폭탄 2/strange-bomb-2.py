import sys

input = sys.stdin.readline

# 선언부
def solve():
    result = -1
    for i in range(N):
        for j in range(1, K + 1):
            if i + j >= N:
                break
            if bombs[i] == bombs[i + j]:
                result = max(result, bombs[i])
                break
    print(result)

# 구현부
N, K = map(int, input().split())
bombs = [int(input()) for _ in range(N)]
solve()
