import sys

input = sys.stdin.readline

# 선언부
def calculate_distance(cx: int, cy: int, nx: int, ny: int):
    return abs(cx - nx) + abs(cy - ny)

def solve():
    result = int(1e9)
    for i in range(1, N - 1):
        cx, cy = check_points[0]
        temp_distance = 0
        for j in range(1, N):
            if j == i:
                continue
            nx, ny = check_points[j]
            temp_distance += calculate_distance(cx, cy, nx, ny)
            cx, cy = nx, ny
        result = min(result, temp_distance)
    print(result)

# 구현부
N = int(input())
check_points = []
for _ in range(N):
    x, y = map(int, input().split())
    check_points.append((x, y))
solve()
