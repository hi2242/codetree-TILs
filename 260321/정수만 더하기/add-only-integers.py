import sys

input = sys.stdin.readline

# 선언부

# 구현부
A = input().rstrip()
count = 0
for c in A:
    if '0' <= c <= '9':
        count += int(c)
print(count)
