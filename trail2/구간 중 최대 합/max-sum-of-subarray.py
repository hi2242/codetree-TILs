import sys

input = sys.stdin.readline

# 선언부
def solve():
    result = 0
    for i in range(N - K + 1):
        temp = 0
        for j in range(K):
            temp += numbers[i + j]
        result = max(result, temp)
    print(result)

# 구현부
N, K = map(int, input().split())
numbers = list(map(int, input().split()))
solve()
