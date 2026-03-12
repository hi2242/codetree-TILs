import sys

input = sys.stdin.readline

# 선언부

# 입력부
N = int(input())

# 호출부
for i in range(1, N + 1):
    if i % 2 == 0 or i % 3 == 0:
        print(1, end=' ')
    else:
        print(0, end=' ')