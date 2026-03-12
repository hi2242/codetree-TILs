import sys

input = sys.stdin.readline

# 선언부

# 입력부
A, B = map(int, input().split())

# 호출부
if A > 0:
    for _ in range(B):
        print(A, end='')
else:
    print(0)