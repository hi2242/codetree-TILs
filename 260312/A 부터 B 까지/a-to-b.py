import sys

input = sys.stdin.readline

# 선언부

# 입력부
A, B = map(int, input().split())

# 호출부
while A <= B:
    print(A, end=' ')
    if A % 2 == 1:
        A *= 2
    else:
        A += 3