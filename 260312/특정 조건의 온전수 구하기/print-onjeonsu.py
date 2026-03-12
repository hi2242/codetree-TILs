import sys

input = sys.stdin.readline

# 선언부

# 입력부
N = int(input())

# 호출부
for i in range(1, N + 1):
    if i % 2 == 0 or i % 10 == 5 or (i % 3 == 0 and i % 9 != 0):
        continue

    print(i, end=' ')