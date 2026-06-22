import sys

input = sys.stdin.readline

# 선언부
MAX_DISTANCE = float('inf')

def calc_max_distance():
    curr, result = 0, 0
    start, end = 0, 0
    for i in range(1, N):
        if seats[i] == 1:
            if result < i - curr:
                result = i - curr
                start, end = curr, i
            curr = i
    seats[(end - start) // 2 + start] = 1

def calc_min_distance():
    curr, result = 0, MAX_DISTANCE
    for i in range(1, N):
        if seats[i] == 1:
            result = min(result, i - curr)
            curr = i
    return result

def solve():
    calc_max_distance()
    print(calc_min_distance())

# 구현부
N = int(input())
seats = list(map(int, input().rstrip()))
solve()
