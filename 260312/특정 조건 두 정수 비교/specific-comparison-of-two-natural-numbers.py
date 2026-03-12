import sys

input = sys.stdin.readline

A, B = map(int, input().split())

first_result = 1 if A < B else 0
second_result = 1 if A == B else 0

print(first_result, second_result)