import sys

input = sys.stdin.readline

def multi_input(n: int):
    return [input() for _ in range(n)]

a, b = map(float, multi_input(2))

print('High' if a >= 1.0 and b >= 1.0 else \
 'Middle' if a >= 0.5 and b >= 0.5 else 'Low')