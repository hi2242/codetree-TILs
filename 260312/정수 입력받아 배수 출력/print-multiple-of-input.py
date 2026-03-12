import sys

input = sys.stdin.readline

# 선언부

# 입력부
N = int(input())

# 구현부
for i in range(N, 5 * N + 1, N):
    print(i, end=' ')