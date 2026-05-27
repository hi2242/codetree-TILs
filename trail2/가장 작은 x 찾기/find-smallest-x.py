import sys
import math

input = sys.stdin.readline

# 선언부
def solve():
    start = 0
    for i in range(N):
        start = max(start, segments[i][0] / (2 ** (i + 1)))
    print(math.ceil(start))

# 구현부
N = int(input())
segments = [tuple(map(int, input().split())) for _ in range(N)]
solve()
