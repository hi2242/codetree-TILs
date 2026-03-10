import sys

input = sys.stdin.readline

a, b, c = map(int, input().split())

acc = a + b + c
avg = int(acc / 3)
print(acc, avg, acc - avg, sep='\n')