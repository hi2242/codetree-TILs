import sys

input = sys.stdin.readline

a, b, c = map(int, input().split())

print(a if a >= b >= c or a >= c >= b else \
b if b >= a >= c or b >= c >= a else c)