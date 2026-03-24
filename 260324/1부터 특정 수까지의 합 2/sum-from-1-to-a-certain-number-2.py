import sys

input = sys.stdin.readline

# 선언부
def solve(acc: int, n: int):
    if n == 0:
        print(acc)
        return
    acc += n
    solve(acc, n - 1)

# 구현부
N = int(input())
solve(0, N)
