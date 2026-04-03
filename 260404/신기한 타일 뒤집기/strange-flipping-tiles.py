import sys

input = sys.stdin.readline

# 선언부
def solve(value: int, direction: str):
    global black_count, white_count, curr_pos

    if direction == 'R':
        for i in range(value):
            if tiles[curr_pos + i] == 'W':
                white_count -= 1
            if tiles[curr_pos + i] == 'G' or tiles[curr_pos + i] == 'W':
                tiles[curr_pos + i] = 'B'
                black_count += 1
        curr_pos += value - 1
    else:
        for i in range(value):
            if tiles[curr_pos - i] == 'B':
                black_count -= 1
            if tiles[curr_pos - i] == 'G' or tiles[curr_pos - i] == 'B':
                tiles[curr_pos - i] = 'W'
                white_count += 1 
        curr_pos -= value - 1
    
# 구현부
N = int(input())
tiles = ['G' for _ in range(200001)]
curr_pos = 100000
black_count, white_count = 0, 0
for _ in range(N):
    line = input().rstrip().split()
    solve(int(line[0]), line[1])

print(white_count, black_count)
