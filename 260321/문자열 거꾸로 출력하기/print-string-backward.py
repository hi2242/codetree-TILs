import sys

input = sys.stdin.readline

# 선언부
 
# 구현부
while True:
    s = input().rstrip()
    if s == 'END':
        break
    print(s[::-1])
    