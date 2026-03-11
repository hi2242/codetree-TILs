import sys

input = sys.stdin.readline

N = int(input())
result = None

if N >= 3000:
    result = 'book'
elif N >= 1000:
    result = 'mask'
elif N >= 500:
    result = 'pen'
else:
    result = 'no'

print(result)