import sys

input = sys.stdin.readline

# 선언부
def solve(value: int, direction: str, curr_idx: int):
    if direction == 'R':
        for i in range(value):
            area[curr_idx + i] += 1
        curr_idx += value
    else:
        for i in range(value):
            area[curr_idx - i - 1] += 1
        curr_idx -= value
    return curr_idx

def print_area():
    count = 0
    for i in area:
        if i >= 2:
            count += 1
    print(count)

# 구현부
N = int(input())
area = [0 for _ in range(2001)]
curr_idx = 1000
for _ in range(N):
    line = input().rstrip().split()
    curr_idx = solve(int(line[0]), line[1], curr_idx)
print_area()
