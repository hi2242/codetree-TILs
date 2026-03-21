import sys

input = sys.stdin.readline

# 선언부

# 구현부
s = input().rstrip()
a = list(s)
a[1] = 'a'
a[-2] = 'a'
print(*a, sep='')
