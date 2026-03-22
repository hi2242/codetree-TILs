import sys

input = sys.stdin.readline

# 선언부
def solve(a: int, b: int, c: int):
    if a <= b <= c or a <= c <= b:
        print(a)
    elif b <= a <= c or b <= c <= a:
        print(b)
    else:
        print(c)

# 구현부
a, b, c = map(int, input().split())
solve(a, b, c)
