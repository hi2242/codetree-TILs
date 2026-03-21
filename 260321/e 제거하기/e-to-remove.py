import sys

input = sys.stdin.readline

# 선언부

# 구현부
s = input().rstrip()
for i in range(len(s)):
    if s[i] == 'e':
        s = s[:i] + s[i + 1:]
        break
print(s)
