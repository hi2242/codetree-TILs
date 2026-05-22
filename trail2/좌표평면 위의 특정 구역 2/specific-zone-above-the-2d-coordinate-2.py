import sys

input = sys.stdin.readline

INF = float('inf')

# 선언부
def calc_area(x_pos: list[int], y_pos: list[int]) -> int:
    return (max(x_pos) - min(x_pos)) * (max(y_pos) - min(y_pos))

def solve():
    area = INF
    for i in range(N):
        x_pos, y_pos = [], []
        for j in range(N):
            if i == j:
                continue
            x, y = segments[j]
            x_pos.append(x)
            y_pos.append(y)
        else:
            area = min(area, calc_area(x_pos, y_pos))
    print(area)

# 구현부
N = int(input())
segments = []
for _ in range(N):
    segments.append(tuple(map(int, input().split())))
solve()
