import sys

input = sys.stdin.readline

# 선언부
MAX_NUM = 1000000

def find_max_count(bombs_count):
    max_count, idx = 0, 0
    for i in range(MAX_NUM + 1):
        if bombs_count[i] > 1 and max_count <= bombs_count[i]:
            max_count = bombs_count[i]
            idx = i
    return max_count, idx

def solve():
    result = 0
    max_count = 0
    for i in range(N - K):
        bombs_count = [0 for _ in range(MAX_NUM + 1)]
        bombs_count[bombs[i]] += 1
        for j in range(1, K + 1):
            bombs_count[bombs[i + j]] += 1
        if bombs_count[bombs[i]] < 2:
            continue
        count, idx = find_max_count(bombs_count)
        if max_count < count:
            max_count = count
            result = idx
        elif max_count == count:
            result = max(result, idx)
    print(result)

# 구현부
N, K = map(int, input().split())
bombs = [int(input()) for _ in range(N)]
solve()
