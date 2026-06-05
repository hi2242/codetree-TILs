import sys

input = sys.stdin.readline

# 선언부
def solve():
    is_intersecting = True

    if c > b or a > d:
        is_intersecting = False
    result = max(b, d) - min(a, c) if is_intersecting else (b - a + d - c)
    print(result)
    
# 구현부
a, b = map(int, input().split())
c, d = map(int, input().split())
solve()
