import sys

input = sys.stdin.readline

# 선언부
def solve():
    result = "overlapping"
    if y2 < b1 or x2 < a1 or y1 > b2 or x1 > a2:
        result = "nonoverlapping"
    print(result)

# 구현부
x1, y1, x2, y2 = map(int, input().split())
a1, b1, a2, b2 = map(int, input().split())
solve()
