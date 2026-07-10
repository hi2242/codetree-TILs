import sys

input = sys.stdin.readline

# 선언부
INF = float('inf')

def calc_distance():
    prev_pos = None
    distance = INF
    for i in range(N):
        if seats[i] == '1' and prev_pos == None:
            prev_pos = i
            continue
        if seats[i] == '1':
            if distance > i - prev_pos:
                distance = i - prev_pos
            prev_pos = i
    return distance

def find():
    start, end, prev_pos = None, None, None
    c_s, c_e = None, None
    distance = 0

    # 1간 거리 뽑기
    for i in range(N):
        if seats[i] == '1' and start == None:
            start, prev_pos = i, i
            continue
        if seats[i] == '1':
            if distance < i - prev_pos:
                distance = i - prev_pos
                c_s, c_e = prev_pos, i
            prev_pos = i
    distance = 0
    if c_s != None and c_e != None:
        seats[(c_e + c_s) // 2] = '1'
        distance = calc_distance()
        seats[(c_e + c_s) // 2] = '0'
    # 시작만 1인 경우
    if seats[N - 1] == '0':
        seats[N - 1] = '1'
        distance = max(distance, calc_distance())
        seats[N - 1] = '0'
    # 끝만 1인 경우
    if seats[0] == '0':
        seats[0] = '1'
        distance = max(distance, calc_distance())
        seats[0] = '0'
    

    return distance

def solve():
  distance = find()
  print(distance)

# 구현부
N = int(input())
seats = list(str(input().rstrip()))
solve()
