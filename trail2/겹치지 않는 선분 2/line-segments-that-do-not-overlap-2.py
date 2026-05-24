import sys

input = sys.stdin.readline

# 선언부
def is_cross(l1: tuple[int, int], l2: tuple[int, int]) -> bool:
    result = False
    if (l1[0] < l2[0] and l1[1] > l2[1]) or (l1[0] > l2[0] and l1[1] < l2[1]):
        result = True
    return result

def solve():
    result = 0
    lines_count = len(lines)
    for i in range(lines_count):
        for j in range(lines_count):
            if i == j:
                continue
            if is_cross(lines[i], lines[j]):
                break
        else:
            result += 1
    print(result)

# 구현부
N = int(input())
lines = [tuple(map(int, input().split())) for _ in range(N)]
solve()
