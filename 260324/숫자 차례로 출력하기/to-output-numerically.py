import sys

input = sys.stdin.readline

# 선언부
def solve1(n: int):
    if n == 0:
        return
    solve1(n - 1)
    print(n, end=' ')

def solve2(n: int):
    if n == 0:
        return
    print(n, end=' ')
    solve2(n - 1)

# 구현부
N = int(input())
solve1(N)
print()
solve2(N)
