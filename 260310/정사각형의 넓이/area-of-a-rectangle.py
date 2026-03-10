import sys

input = sys.stdin.readline

N = int(input())

print(N ** 2)

if N < 5:
    print('tiny')