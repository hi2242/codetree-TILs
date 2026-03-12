import sys

input = sys.stdin.readline

# 선언부

# 입력부
A, B = map(int, input().split())

# 호출부
prod = 1
for i in range(1, B + 1):
    if i % A == 0:
        prod *= i

print(prod) 