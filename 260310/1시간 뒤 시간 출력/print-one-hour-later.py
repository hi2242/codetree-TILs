import sys

input = sys.stdin.readline

h, m = map(int, input().split(':'))

print(f'{h + 1}:{m}')