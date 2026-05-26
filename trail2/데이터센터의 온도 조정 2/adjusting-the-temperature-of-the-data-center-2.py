import sys

input = sys.stdin.readline

INF = float('inf')
# 선언부
def work(i: int, j: int) -> int:
    start, end = temperatures[j]
    result = 0
    if i < start:
        result = C
    elif start <= i <= end:
        result = G
    else:
        result = H
    return result
    
def solve():
    result = 0
    for i in range(min_temp - 1, max_temp + 2):
        throughput = 0
        for j in range(N):
            throughput += work(i, j)
        result = max(result, throughput)
    print(result)

# 구현부
N, C, G, H = map(int, input().split())
min_temp, max_temp, temperatures = INF, 0, []
for _ in range(N):
    start, end = map(int, input().split())
    min_temp = min(min_temp, start)
    max_temp = max(max_temp, end)
    temperatures.append((start, end))
solve()
