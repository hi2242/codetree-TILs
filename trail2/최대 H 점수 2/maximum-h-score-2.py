import sys

input = sys.stdin.readline

# 선언부
MAX_H = 100
def solve():
    result = 0
    for h in range(MAX_H + 1):
        count = 0
        extra = L
        for i in range(N):
            if numbers[i] >= h:
                count += 1
            elif extra > 0 and numbers[i] + 1 == h:
                extra -= 1
                count += 1
        if count >= h:
            result = h
    print(result)

# 구현부
N, L = map(int, input().split())
numbers = list(map(int, input().split()))
solve()
