import sys

input = sys.stdin.readline

INF = float('inf')
MAX_VALUE = 100

# 선언부
def sort_axis(p: tuple[int, int], x: int, y: int, axis_info: list[int]) -> None:
    if p[0] > x and p[1] > y:
        axis_info[0] += 1
    elif p[0] < x and p[1] > y:
        axis_info[1] += 1
    elif p[0] < x and p[1] < y:
        axis_info[2] += 1
    elif p[0] > x and p[1] < y:
        axis_info[3] += 1
def solve():
    result = INF
    for x in range(2, MAX_VALUE + 1, 2):
        for y in range(2, MAX_VALUE + 1, 2):
            axis_info = [0 for _ in range(4)]
            for p in points:
                sort_axis(p, x, y, axis_info)
            result = min(result, max(axis_info))
    print(result)

# 구현부
N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]
solve()
