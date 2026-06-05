import sys

input = sys.stdin.readline

# 선언부
def solve():
    result = "intersecting"
    if x2 < x3 or x4 < x1:
        result = "nonintersecting"
    print(result)

# 구현부
x1, x2, x3, x4 = map(int, input().split())
solve()
