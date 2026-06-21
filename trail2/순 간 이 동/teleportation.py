import sys

input = sys.stdin.readline

# 선언부
def solve():
    first = abs(B - A)
    second = abs(B - y) + abs(x - A)
    third = abs(B - x) + abs(y - A)
    print(min(first, second, third))

# 구현부
A, B, x, y = map(int, input().split())
solve()
