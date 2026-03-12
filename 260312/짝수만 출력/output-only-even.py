import sys

input = sys.stdin.readline

# 선언부

# 입력부
A, B = map(int, input().split())

# 호출부
while A <= B:
    print(A, end=' ')
    A += 2