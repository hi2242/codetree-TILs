import sys

input = sys.stdin.readline

# 선언부
def check(speed, pos):
    result = "DOWN"
    rest_distance = X - pos
    need_distance = (speed * (speed + 1)) / 2
    if rest_distance - (speed + 1) >= need_distance:
        result = "UP"
    elif speed == 1 or rest_distance >= need_distance:
        result = "STAY"
    return result

def solve():
    curr_speed, curr_pos, time = 1, 1, 1
    while True:
        # print(curr_speed, curr_pos)
        if curr_pos == X:
            break
        cmd = check(curr_speed, curr_pos)
        if cmd == "UP":
            curr_speed += 1
        elif cmd == "DOWN":
            curr_speed -= 1
        curr_pos += curr_speed
        time += 1
    print(time)

# 구현부
X = int(input())
solve()
