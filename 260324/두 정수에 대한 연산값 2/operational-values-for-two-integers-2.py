import sys

input = sys.stdin.readline

# 선언부
def solve(a: int, b: int):
    if a > b:
        a *= 2
        b += 10
    else:
        b *= 2
        a += 10
    return [a, b]

# 구현부
a, b = map(int, input().split())
a, b = solve(a, b)
print(a, b)
