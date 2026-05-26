import sys

input = sys.stdin.readline

# 선언부
def solve():
    result = 0
    for i in range(N):
        acc = numbers[i]
        prev = numbers[i]
        for _ in range(M - 1):
            acc += numbers[prev - 1]
            prev = numbers[prev - 1]
        result = max(result, acc)
    print(result)

# 구현부
N, M = map(int, input().split())
numbers = list(map(int, input().split()))
solve()
