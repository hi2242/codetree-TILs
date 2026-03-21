import sys

input = sys.stdin.readline

# 선언부

# 구현부
a, b = map(int, input().split())
print(str(a + b).count('1'))
