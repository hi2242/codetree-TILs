import sys

input = sys.stdin.readline

# 선언부
def solve(value: int, direction: int, curr_pos: int):
    if direction == 'R':
        for i in range(value):
            tiles[curr_pos + i][1] += 1
            tiles[curr_pos + i][2] = 'B'
        curr_pos += value - 1
    else:
        for i in range(value):
            tiles[curr_pos - i][0] += 1
            tiles[curr_pos - i][2] = 'W'
        curr_pos -= value - 1
    return curr_pos

def print_tiles():
    result = [0, 0, 0]
    for white, black, last in tiles:
        if white >= 2 and black >= 2:
            result[2] += 1
        else:
            if last == 'B':
                result[1] += 1
            elif last == 'W':
                result[0] += 1
    print(*result)
    
# 구현부
N = int(input())
tiles = [[0, 0, ''] for _ in range(200001)]
curr_pos = 100000
for _ in range(N):
    line = input().rstrip().split()
    curr_pos = solve(int(line[0]), line[1], curr_pos)
print_tiles()
