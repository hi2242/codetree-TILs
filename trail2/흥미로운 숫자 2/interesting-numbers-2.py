import sys

input = sys.stdin.readline

# 선언부
def solve():
    result = 0
    for i in range(len(str(X)), len(str(Y)) + 1):
        for a in '0123456789':
            for j in range(i):
                for b in '0123456789':
                    if a == b:
                        continue
                    temp = a * j + b + a * (i - j - 1)
                    if int(temp[0]) != 0 and X <= int(temp) <= Y:
                        result += 1
    print(result)

# 구현부
X, Y = map(int, input().split())
solve()
