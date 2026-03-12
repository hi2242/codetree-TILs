import sys

input = sys.stdin.readline

A = int(input())
B, C, D, E = map(int, input().split())

print(1 if A > B else 0)
print(1 if A > C else 0)
print(1 if A > D else 0)
print(1 if A > E else 0)