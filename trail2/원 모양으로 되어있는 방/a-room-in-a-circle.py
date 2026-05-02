import sys

input = sys.stdin.readline

# 선언부
def solve():
    result = int(1e9)
    for i in range(N):
        temp = 0
        for j in range(N):
            temp += head_counts[(i + j) % N] * j
        result = min(result, temp)
    print(result)

# 구현부
N = int(input())
head_counts = []
for _ in range(N):
    head_counts.append(int(input()))
solve()
