import sys

input = sys.stdin.readline

a, b = map(int, input().split())

first_info, second_info = None, None

if a % 2 == 0:
    first_info = 'even'
else:
    first_info = 'odd'

if b % 2 == 0:
    second_info = 'even'
else:
    second_info = 'odd'

print(first_info, second_info, sep='\n')