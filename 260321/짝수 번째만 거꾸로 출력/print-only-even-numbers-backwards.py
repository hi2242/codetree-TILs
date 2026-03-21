import sys

input = sys.stdin.readline

# 선언부

# 구현부
s = input().rstrip()
for i in range(len(s) - 1, -1, -1):
    if (i + 1) % 2 == 0:
        print(s[i], end='')
        