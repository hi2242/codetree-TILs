import sys
import math

input = sys.stdin.readline

# 선언부

# 입력부
A, B = map(int, input().split())

# 호출부
print(A // B, end='.')
A %= B
A *= 10

for _ in range(20):
    print(A // B, end='')
    A %= B
    A *= 10