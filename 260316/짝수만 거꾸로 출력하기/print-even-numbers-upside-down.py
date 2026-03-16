import sys

input = sys.stdin.readline

# 선언부
def solve(n: int, n_list: list[int]):
    for i in range(n - 1, -1, -1):
        if n_list[i] % 2 == 0:
            print(n_list[i], end=' ')

# 구현부
N = int(input())
number_list = list(map(int, input().split()))
solve(N, number_list)
