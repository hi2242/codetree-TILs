import sys

input = sys.stdin.readline

# 선언부
def solve(start: int, end: int):
    count = 0
    for i in range(start, end + 1):
        s = str(i)
        if i % 3 == 0:
            count += 1
        elif s.count('3') or s.count('6') or s.count('9'):
            count += 1
    print(count)

# 호출부
A, B = map(int, input().split())
solve(A, B)
