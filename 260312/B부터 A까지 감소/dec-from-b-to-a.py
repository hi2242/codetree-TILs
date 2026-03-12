import sys

input = sys.stdin.readline

# 선언부

# 입력부
A, B = map(int, input().split())

# 구현부
for i in range(B, A - 1, -1):
    print(i, end=' ')