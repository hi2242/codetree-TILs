# 문제 정보
# 회의가 끝나자마자 다른 회의 시작 가능

# 입력 정보
# N -> 회의 횟수
# s, e -> 회의 시작과 끝

# 출력 정보
# 최대로 회의를 돌리는 횟수

import sys

input = sys.stdin.readline

def solve():
    answer = 0
    curr_time = 0
    for s, e in schedule:
        if curr_time <= s:
            curr_time = e
            answer += 1
    print(answer)

N = int(input())
schedule = [list(map(int, input().split())) for _ in range(N)]
schedule.sort(key = lambda x: (x[1], x[0]))
solve()
