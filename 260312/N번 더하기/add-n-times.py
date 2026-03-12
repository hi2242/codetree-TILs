import sys

input = sys.stdin.readline

# 선언부

# 입력부
A, N = map(int, input().split())

# 호출부
for _ in range(N):
    A += N
    print(A)