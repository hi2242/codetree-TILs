import sys

input = sys.stdin.readline

A = int(input())

print('YES' if A % 3 == 0 else 'NO')
print('YES' if A % 5 == 0 else 'NO')
