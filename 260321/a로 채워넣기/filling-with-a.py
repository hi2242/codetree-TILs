import sys

input = sys.stdin.readline

# 선언부

# 구현부
s = input().rstrip()
s[1] = 'a'
s[-2] = 'a'
print(s)
