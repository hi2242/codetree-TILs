import sys

input = sys.stdin.readline

# 선언부
def solve(n: int, m: int):
    return m, n
# 구현부
n, m = map(int, input().split())
n, m = solve(n, m)
print(n, m)
