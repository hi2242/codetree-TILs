import sys

input = sys.stdin.readline

m, d, y = map(int, input().split('-'))

print(f'{y}.{m}.{d}')