import sys

input = sys.stdin.readline

def multi_input(n: int):
    return [input().rstrip() for _ in range(n)]

S, T = multi_input(2)

print(f"""{T}
{S}""")