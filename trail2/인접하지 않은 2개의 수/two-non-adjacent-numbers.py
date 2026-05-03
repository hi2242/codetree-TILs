import sys

input = sys.stdin.readline

# 선언부
def solve():
    result = 0
    for i in range(N):
        for j in range(i + 2, N):
            result = max(result, numbers[i] + numbers[j])
    print(result)

# 구현부
N = int(input())
numbers = list(map(int, input().split()))
solve()
