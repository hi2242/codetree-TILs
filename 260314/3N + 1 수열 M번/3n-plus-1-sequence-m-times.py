import sys

input = sys.stdin.readline

# 선언부
def solve(n: int):
    count = 0
    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = n * 3 + 1
        count += 1
    return count

# 구현부
M = int(input())
for _ in range(M):
    N = int(input())
    print(solve(N))
