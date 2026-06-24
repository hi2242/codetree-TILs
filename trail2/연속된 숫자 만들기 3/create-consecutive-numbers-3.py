import sys

input = sys.stdin.readline

# 선언부
def move(f_d, s_d):
    return max(f_d - 1, s_d - 1)

def solve():
    move_count = 0
    f_distance, s_distance = positions[1] - positions[0], positions[2] - positions[1]
    print(move(f_distance, s_distance))

# 구현부
positions = list(map(int, input().split()))
solve()
