import sys

input = sys.stdin.readline

# 선언부
def solve(N: int, n_list: list[int], T: int):
    max_count, count = 0, 0
    for i in range(N):
        if n_list[i] > T:
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0
    print(max_count)

# 구현부
N, T = map(int, input().split())
n_list = list(map(int, input().split()))
solve(N, n_list, T)
