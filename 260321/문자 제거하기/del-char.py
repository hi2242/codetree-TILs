import sys

input = sys.stdin.readline

# 선언부

# 구현부
s = input().rstrip()
a = list(s)
while len(a) > 1:
    target = int(input())
    if target >= len(a):
        a.pop()
    else:
        a.pop(target)
    print(*a, sep='')
