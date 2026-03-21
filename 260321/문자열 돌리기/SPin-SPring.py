import sys

input = sys.stdin.readline

# 선언부

# 구현부
s = input().rstrip()
L = len(s)
print(s)
for _ in range(L):
    s = s[-1] + s[:-2] 
    print(s)
