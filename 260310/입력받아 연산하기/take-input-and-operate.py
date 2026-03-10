import sys

input = sys.stdin.readline

def multi_input(n: int):
    return [input() for _ in range(n)]

a, b = map(int, multi_input(2))
a += 87
b %= 10

print(a, b, sep = '\n')