import sys

input = sys.stdin.readline

# 선언부
def solve(n: int):
    for i in range(2, n + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i, end=' ')

# 구현부
N = int(input())
solve(N)