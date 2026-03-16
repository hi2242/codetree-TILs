import sys

input = sys.stdin.readline

# 선언부
def solve(n_list: list[int]):
    for i in range(len(n_list) - 1, -1, -1):
        if n_list[i] == 0:
            continue
        print(n_list[i], end=' ')

# 구현부
number_list = list(map(int, input().split()))
solve(number_list)
