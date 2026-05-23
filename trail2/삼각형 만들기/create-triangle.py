import sys

input = sys.stdin.readline

# 선언부
def is_right(p1: tuple[int], p2: tuple[int], p3: tuple[int]) -> bool:
    return len({p1[0], p2[0], p3[0]}) == 2 and len({p1[1], p2[1], p3[1]}) == 2

def calc_extend(p1: tuple[int], p2: tuple[int]) -> int:
    return (abs(p1[0] - p2[0]) * abs(p1[1] - p2[1])) / 2

def calc_tri(p1: tuple[int], p2: tuple[int], p3: tuple[int]) -> int:
    width = max(p1[0], p2[0], p3[0]) - min(p1[0], p2[0], p3[0])
    height = max(p1[1], p2[1], p3[1]) - min(p1[1], p2[1], p3[1])
    return width * height - (calc_extend(p1, p2) + calc_extend(p2, p3) + calc_extend(p3, p1))

def solve():
    result = 0
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                if is_right(point_list[i], point_list[j], point_list[k]):
                    result = max(result, calc_tri(point_list[i], point_list[j], point_list[k]))
    print(int(result * 2))

# 구현부
N = int(input())
point_list = []
for _ in range(N):
    point_list.append(tuple(map(int, input().split())))
solve()
