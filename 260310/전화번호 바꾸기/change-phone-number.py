import sys

input = sys.stdin.readline

front, middle, end = input().rstrip().split('-')

print(front, end, middle, sep = '-')