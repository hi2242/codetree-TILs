import sys

input = sys.stdin.readline

# 선언부
MAX_HEIGHT = 100
MAX_HEIGHT_DIFF = 17
INF = float('inf')

def calc_cost(target_height, height):
    return (target_height - height) ** 2

def solve():
    max_height, min_height = max(hills), min(hills)
    result = INF
    diff = max_height - min_height

    if diff <= MAX_HEIGHT_DIFF:
        print(0)
        return

    for i in range(diff - MAX_HEIGHT_DIFF + 1):
        target_bottom_height, target_top_height = min_height + i, max_height - (diff - MAX_HEIGHT_DIFF - i)
        acc = 0
        for height in hills:
            if height < target_bottom_height:
                acc += calc_cost(target_bottom_height, height)
            elif height > target_top_height:
                acc += calc_cost(target_top_height, height)
        result = min(result, acc)
    print(result)
            
# 구현부
N = int(input())
hills = [int(input()) for _ in range(N)]
heights = [0 for _ in range(MAX_HEIGHT + 1)]
for height in hills:
    heights[height] += 1
solve()
