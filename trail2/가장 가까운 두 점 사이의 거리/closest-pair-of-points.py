import sys

input = sys.stdin.readline

INF = float('inf')
# 선언부
def calc_distance(p1: tuple[int, int], p2: tuple[int, int]) -> int:
    return abs(p1[0] - p2[0]) ** 2 + abs(p1[1] - p2[1]) ** 2

def solve():
    result = INF
    for i in range(N):
        for j in range(N):
            if len({i, j}) != 2:
                continue
            result = min(result, calc_distance(point_list[i], point_list[j]))
    print(result)

# 구현부
N = int(input())
point_list = []
for _ in range(N):
    point_list.append(tuple(map(int, input().split())))
solve()
