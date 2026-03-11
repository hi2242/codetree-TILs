import sys

input = sys.stdin.readline

vision = float(input())

if vision >= 1.0:
    print('High')
elif vision >= 0.5:
    print('Middle')
else:
    print('Low')