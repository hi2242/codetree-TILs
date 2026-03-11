import sys

input = sys.stdin.readline

alphabet = input().rstrip()
result = None

if alphabet == 'S':
    result = 'Superior'
elif alphabet == 'A':
    result = 'Excellent'
elif alphabet == 'B':
    result = 'Good'
elif alphabet == 'C':
    result = 'Usually'
elif alphabet == 'D':
    result = 'Effort'
else:
    result = 'Failure'

print(result)