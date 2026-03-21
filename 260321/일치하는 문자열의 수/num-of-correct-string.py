import sys

input = sys.stdin.readline

# 선언부

# 구현부
n, A = input().split()
n = int(n)
count = 0
for _ in range(n):
    s = input().rstrip()
    if A == s:
        count += 1
print(count)
