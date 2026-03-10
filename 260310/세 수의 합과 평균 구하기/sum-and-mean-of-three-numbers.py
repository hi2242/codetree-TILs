import sys

input = sys.stdin.readline

A = list(map(int, input().split()))

print(sum(A), sum(A) // len(A), sep='\n')