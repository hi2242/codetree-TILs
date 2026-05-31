import sys

input = sys.stdin.readline

# 선언부
MAX_NUM = 1000000

def check_between(bombs_count, exploded, start, n):
    for i in range(n + 1):
        if not exploded[start + i]:
            bombs_count[bombs[start + i]] += 1
            exploded[start + i] = 1

def find_max_count(bombs_count):
    max_count, idx = 0, 0
    for i in range(MAX_NUM + 1):
        if bombs_count[i] >= 2 and max_count <= bombs_count[i]:
            max_count, idx = bombs_count[i], i
    print(idx)

def solve():
    bombs_count = [0 for _ in range(MAX_NUM + 1)]
    exploded = [0 for _ in range(N)]
    for i in range(N - K):
        for j in range(K, 0, -1):
            if bombs[i] == bombs[i + j]:
                check_between(bombs_count, exploded, i, j)
                break
    find_max_count(bombs_count)

# 구현부
N, K = map(int, input().split())
bombs = [int(input()) for _ in range(N)]
solve()
