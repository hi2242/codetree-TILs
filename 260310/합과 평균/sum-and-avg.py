import sys

input = sys.stdin.readline

acc = sum(map(int, input().split()))

print(f'{acc} {acc / 2:.1f}')