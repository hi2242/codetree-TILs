import sys

input = sys.stdin.readline

# 선언부

# 입력부
B, A = map(int, input().split())

# 구현부
for i in range(B, A - 1, -2):
    print(i, end=' ')