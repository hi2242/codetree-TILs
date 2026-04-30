import sys

input = sys.stdin.readline

# 선언부
def translate(k: int):
    acc = 0
    for i in range(len(a)):
        if i == k:
            x = 1 if int(a[i]) == 0 else 0
            acc += x * (2 ** (len(a) - 1 - i))
        else:
            acc += int(a[i]) * (2 ** (len(a) - 1 - i))
    return acc

def solve():
    result = 0
    for i in range(len(a)):
        result = max(result, translate(i))
    print(result)

# 구현부
a = input().rstrip()
solve()
