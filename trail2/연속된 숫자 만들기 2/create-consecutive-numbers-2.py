import sys

input = sys.stdin.readline

# 선언부
def solve():
    count = 0
    sorted_a, sorted_b, sorted_c = sorted([a, b, c])
    if sorted_a + 1 == sorted_b and sorted_b + 1 == sorted_c:
        count = 0
    elif sorted_a == sorted_b - 2 or sorted_c == sorted_b + 2:
        count = 1
    else:
        count = 2
    print(count)

# 구현부
a, b, c = map(int, input().split())
solve()
