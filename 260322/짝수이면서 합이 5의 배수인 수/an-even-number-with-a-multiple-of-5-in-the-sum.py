import sys

input = sys.stdin.readline

# 선언부
def solve(n: str):
    temp = list(map(int, n))

    if temp[-1] % 2 == 0 and sum(temp) % 5 == 0:
        print('Yes')
    else:
        print('No')

# 구현부
n = input().rstrip()
solve(n)
