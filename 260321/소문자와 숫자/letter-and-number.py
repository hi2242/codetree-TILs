import sys

input = sys.stdin.readline

# 선언부

# 구현부
s = input().rstrip()
for c in s:
    if 'A' <= c <= 'Z':
        print(c.lower(), end='')
    elif 'a' <= c <= 'z' or '0' <= c <= '9':
        print(c, end='')
