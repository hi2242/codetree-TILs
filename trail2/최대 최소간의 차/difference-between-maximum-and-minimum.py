import sys

input = sys.stdin.readline

# 선언부
def solve():
    h, l = max(numbers), min(numbers)
    diff = h - l
    result = 0
    for i in range(l, h - K + 1):
        cost = 0
        for n in numbers:
            if n < i:
                cost += i - n
            elif n > i + K:
                cost += n - (i + K)
        if result == 0:
            result = cost
        else:
            result = min(result, cost)
    print(result)

# 구현부
N, K = map(int, input().split())
numbers = list(map(int, input().split()))
solve()
