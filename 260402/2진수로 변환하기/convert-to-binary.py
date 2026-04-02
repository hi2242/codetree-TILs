import sys

input = sys.stdin.readline

# 선언부
def solve(N: int):
    result = ''
    temp = N
    while True:
        result = str(temp % 2) + result
        temp //= 2
        if temp == 0:
            break
    print(result)

# 구현부
N = int(input())
solve(N)
