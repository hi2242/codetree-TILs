import sys

input = sys.stdin.readline

# 선언부

# 입력부
A, B = map(int, input().split())

# 구현부
for i in range(A, B + 1, 2):
    print(i, end=' ')