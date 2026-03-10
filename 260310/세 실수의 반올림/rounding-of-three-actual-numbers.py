import sys

input = sys.stdin.readline

def multi_input(n: int):
    return [input() for _ in range(n)]

a, b, c = map(float, multi_input(3))

print(f"""{a:.3f}
{b:.3f}
{c:.3f}""")