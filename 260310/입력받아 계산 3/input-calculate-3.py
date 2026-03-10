import sys

input = sys.stdin.readline

def multi_input(n: int):
    return [input() for _ in range(n)]

lines = multi_input(2)
a, b = map(int, lines)

print(a * b)