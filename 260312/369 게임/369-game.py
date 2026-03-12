import sys

input = sys.stdin.readline

# 선언부

# 입력부
N = int(input())

# 호출부
for i in range(1, N + 1):
    if i % 3 == 0 or \
    i // 100 == 3 or \
    i // 100 == 6 or \
    i // 100 == 9 or \
    i // 10 == 3 or \
    i // 10 == 6 or \
    i // 10 == 9 or \
    i % 10 == 3 or \
    i % 10 == 6 or \
    i % 10 == 9:
        print(0, end=' ')
    else:
        print(i, end=' ')