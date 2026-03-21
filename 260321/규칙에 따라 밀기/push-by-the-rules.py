import sys

input = sys.stdin.readline

# 선언부

# 구현부
A = input().rstrip()
cmd = input().rstrip()
for c in cmd:
    if c == 'L':
        A = A[1:] + A[0]
    elif c == 'R':
        A = A[-1] + A[:-1]
print(A)
