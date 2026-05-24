import sys

input = sys.stdin.readline

# 선언부
def init() -> list[int]:
    result = [0 for _ in range(1001)]
    for s, e in work_time:
        for i in range(s, e):
            result[i] += 1
    return result

def solve():
    timeline = init()
    result = 0
    for i in range(N):
        time = 0
        for j in range(1, 1000):
            if work_time[i][0] <= j < work_time[i][1]:
                if timeline[j] - 1:
                    time += 1
            else:
                if timeline[j]:
                    time += 1
        result = max(result, time)
    print(result)

# 구현부
N = int(input())
work_time = [tuple(map(int, input().split())) for _ in range(N)]
solve()
