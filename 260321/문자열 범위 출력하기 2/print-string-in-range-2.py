import sys

input = sys.stdin.readline

# 선언부

# 구현부
s = input().rstrip()
length = int(input())
if length > len(s):
    length = len(s)
    
for i in range(length):
    print(s[len(s) - 1 - i], end='')
