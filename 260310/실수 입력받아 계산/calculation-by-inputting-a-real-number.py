import sys

input = sys.stdin.readline

def multi_input(n: int):
    return [input() for _ in range(n)]

a, b = map(float, multi_input(2))

print(f'{a + b:.2f}')