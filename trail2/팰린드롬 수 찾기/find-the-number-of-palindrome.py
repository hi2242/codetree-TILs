import sys

input = sys.stdin.readline

# 선언부
def solve():
    result = 0
    for i in range(X, Y + 1):
        string_i = str(i)
        if string_i == string_i[::-1]:
            result += 1
    print(result)

# 구현부
X, Y = map(int, input().split())
solve()
