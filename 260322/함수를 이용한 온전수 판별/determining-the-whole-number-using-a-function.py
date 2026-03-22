import sys

input = sys.stdin.readline

# 선언부
def solve(start: int, end: int):
    count = 0
    for i in range(start, end + 1):
        if i % 2 == 0 or i % 10 == 5 or (i % 3 == 0 and i % 9 == 0):
            continue
        else:
            count += 1
    print(count)
    
# 구현부
A, B = map(int, input().split())
solve(A, B)
