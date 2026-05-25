import sys

input = sys.stdin.readline

MAX_AXIS = 100
# 선언부
def down(temp_axis: list[int], i: int):
    for l in range(lines[i][0], lines[i][1] + 1):
        temp_axis[l] -= 1

def downgrade(temp_axis: list[int], i: int, j: int, k: int):
    for each in [i, j, k]:
        down(temp_axis, each)

def check_duplicate(temp_axis: list[int]) -> int:
    result = 0
    for l in range(MAX_AXIS + 1):
        if temp_axis[l] > 1:
            break
    else:
        result = 1
    return result

def solve():
    result = 0
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                temp_axis = axis.copy()
                downgrade(temp_axis, i, j, k)
                result += check_duplicate(temp_axis)
    print(result)
                
# 구현부
N = int(input())
lines = []
axis = [0 for _ in range(MAX_AXIS + 1)]
for _ in range(N):
    start, end = map(int, input().split())
    lines.append((start, end))
    for i in range(start, end + 1):
        axis[i] += 1
solve()
