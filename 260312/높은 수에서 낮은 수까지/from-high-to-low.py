import sys

input = sys.stdin.readline

# 선언부

# 입력부
A, B = map(int, input().split())

# 호출부
if A < B:
    for i in range(B, A - 1, -1):
        print(i, end=' ')
else:
    for i in range(A, B - 1, -1):
        print(i, end=' ')