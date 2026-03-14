import sys

input = sys.stdin.readline

# 선언부
def solve(start: int, end: int):
    count = 0
    for i in range(start, end + 1):
        acc = 0
        for j in range(1, i):
            if i % j == 0:
                acc += j
        if i == acc:
            count += 1
    return count

# 구현부
start, end = map(int, input().split())
print(solve(start, end))
