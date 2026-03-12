import sys

input = sys.stdin.readline

# 선언부

# 입력부
line = input().split()
C, N = line[0], int(line[1])

# 호출부
if C == 'A':
    for i in range(N):
        print(i + 1, end=' ')
elif C == 'D':
    for i in range(N, 0, -1):
        print(i, end=' ')