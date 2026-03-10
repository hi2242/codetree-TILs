import sys

input = sys.stdin.readline

def multi_input(n: int):
    return [input() for _ in range(n)]

first_line, second_line = multi_input(2)

a, b, c = *map(int, first_line.split()), int(second_line)

print(a, b, c)