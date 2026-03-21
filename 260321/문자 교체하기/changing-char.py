import sys

input = sys.stdin.readline

# 선언부

# 구현부
s1, s2 = input().rstrip().split()
s2 = list(s2)
s2[0], s2[1] = s1[0], s1[1]
print(*s2, sep='')
