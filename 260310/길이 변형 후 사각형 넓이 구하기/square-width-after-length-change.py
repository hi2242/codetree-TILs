import sys

input = sys.stdin.readline

width, height = map(int, input().split())

width += 8
height *= 3

print(width, height, width * height, sep = '\n')