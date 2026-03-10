import sys

input = sys.stdin.readline

y, m, d = map(int, input().split('.'))

print(m, d, y, sep='-')