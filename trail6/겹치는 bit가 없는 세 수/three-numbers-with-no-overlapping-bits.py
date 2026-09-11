# 문제 정보
# n개의 수가 주어졌을 때 서로 다른 3개의 수를 고른다.
# bit가 서로 전혀 겹치지 않는 경우에 한하여 세 수의 합 중 최댓값을 구하기
# 겹친다 == 2진수로 나타내었을 때 단 하나라도 같은 자리에 동시에 1이 있는 경우 의미

# 입력 정보
# n -> 수의 개수
# 모든 수는 다르게 주어짐

# 반환 정보
# answer -> 조건을 만족하는 최대 합

# 풀이 순서
# 1. combination으로 3개를 골라서 조건에 맞는지 확인한다.
# 2. 조건을 만족한다면 최댓값을 갱신한다.

import sys
from itertools import combinations

input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))

def solve():
    answer = 0

    for coms in combinations(numbers, 3):
        if not (coms[0] & coms[1]) and not (coms[1] & coms[2]) and not (coms[0] & coms[2]):
            answer = max(answer, sum(coms))

    print(answer)
solve()