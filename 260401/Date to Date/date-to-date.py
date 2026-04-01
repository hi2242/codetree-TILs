import sys

input = sys.stdin.readline

# 선언부
def solve(m1: int, d1: int, m2: int, d2: int):
    result = 0
    for i in range(m1, m2):
        if i <= 7:
            if i == 2:
                result += 28
            elif i % 2 != 0:
                result += 31
            else:
                result += 30
        else:
            if i % 2 == 0:
                result += 31
            else:
                result += 30
    result = result - (d1 - 1) + d2

    print(result)

# 구현부
m1, d1, m2, d2 = map(int, input().split())
solve(m1, d1, m2, d2)
