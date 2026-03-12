import sys

input = sys.stdin.readline

A, B, C = map(int, input().split())

print(1 if A < B < C else 0)