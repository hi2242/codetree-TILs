import sys

input = sys.stdin.readline

# 선언부

# 구현부
A = input().rstrip()
B = input().rstrip()

count = -1
for i in range(1, len(A) + 1):
    A = A[-1] + A[:-1]
    if A == B:
        count = i
        break
print(count)