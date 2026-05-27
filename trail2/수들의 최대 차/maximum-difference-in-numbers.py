import sys

input = sys.stdin.readline

# 선언부
def solve():
    numbers.sort()
    result = 0
    for i in range(N):
        for j in range(i + 1, N):
            if abs(numbers[i] - numbers[j]) <= K:
                result = max(result, j - i + 1)
    print(result)

# 구현부
N, K = map(int, input().split())
numbers = [int(input()) for _ in range(N)]
solve()
