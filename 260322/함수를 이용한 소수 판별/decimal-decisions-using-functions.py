import sys

input = sys.stdin.readline

# 선언부
def solve(start: int, end: int):
    acc = 0
    for i in range(start, end + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            acc += i
    print(acc)
    
# 구현부
A, B = map(int, input().split())
solve(A, B)
