import sys

input = sys.stdin.readline

# 선언부

# 입력부
N = int(input())

# 호출부
count = 0
for i in range(1, N + 1):
    N //= i
    count += 1
    if N <= 1:
        print(count)
        break