import sys

input = sys.stdin.readline

# 선언부

# 구현부
s = input().rstrip()
s = s[1:] + s[0:1]
print(s)
