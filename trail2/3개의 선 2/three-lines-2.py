import sys

input = sys.stdin.readline

# 선언부
def init() -> list[tuple[int, int]]:
    lines = []
    for i in range(11):
        lines.append((i, -1))
        lines.append((-1, i))
    return lines

def is_inline(i: int, x: list[int], y: list[int], lines: list[tuple[int, int]]):
    if lines[i][0] != -1:
        x.append(lines[i][0])
    else:
        y.append(lines[i][1])

def sort_xy(i: int, j: int, k: int, lines: list[tuple[int, int]]) -> tuple[list[int], list[int]]:
    x, y = [], []
    for parameter in (i, j, k):
        is_inline(parameter, x, y, lines)
    return (x, y)

def solve():
    lines = init()
    L = len(lines)
    result = 0
    for i in range(L):
        for j in range(L):
            for k in range(L):
                if len({i, j, k}) != 3:
                    continue
                x, y = sort_xy(i, j, k, lines)
                for p in points:
                    if p[0] not in x and p[1] not in y:
                        break
                else:
                    result = 1
    print(result)

# 구현부
N = int(input())
points = [list(map(int, input().split())) for _ in range(N)]
solve()
