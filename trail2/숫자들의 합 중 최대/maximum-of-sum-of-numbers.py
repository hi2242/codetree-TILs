import sys

input = sys.stdin.readline

# 선언부
def solve():
    result = 0
    for i in range(X, Y + 1):
        result = max(result, sum(map(int, str(i))))
    print(result)

# 구현부
X, Y = map(int, input().split())
solve()
