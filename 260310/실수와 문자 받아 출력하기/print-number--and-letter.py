import sys

input = sys.stdin.readline

def multi_input(n: int):
    return [input() for _ in range(n)]

a, b, c = multi_input(3)

print(f"""{a.rstrip()}
{float(b):.2f}
{float(c):.2f}""")