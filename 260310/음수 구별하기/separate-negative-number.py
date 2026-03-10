import sys

input = sys.stdin.readline

N = int(input())

if N < 0:
    print(N, 'minus', sep='\n')
else:
    print(N)