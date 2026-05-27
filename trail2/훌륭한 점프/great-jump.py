import sys

input = sys.stdin.readline

# 선언부
INF = float('inf')

def find_under_value(i: int) -> list[int]:
    under_list = []
    for j in range(N):
        if numbers[j] <= i:
            under_list.append(j)
    return under_list

def can_go(under_list: list[int]) -> bool:
    for j in range(1, len(under_list)):
        dist = under_list[j] - under_list[j - 1]
        if dist > K:
            return False
    return True

def solve():
    result = INF
    for i in range(100, max(numbers[0], numbers[-1]) - 1, -1):
        under_list = find_under_value(i)
        if can_go(under_list):
            result = min(result, i)
    print(result)

# 구현부
N, K = map(int, input().split())
numbers = list(map(int, input().split()))
solve()
