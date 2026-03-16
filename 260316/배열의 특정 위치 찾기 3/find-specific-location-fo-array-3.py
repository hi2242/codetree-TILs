import sys

input = sys.stdin.readline

# 선언부
def solve(n_list: list[int]):
    for i in range(len(n_list)):
        if n_list[i] == 0:
            print(n_list[i - 3] + n_list[i - 2] + n_list[i - 1])
            break

# 구현부
number_list = list(map(int, input().split()))
solve(number_list)
