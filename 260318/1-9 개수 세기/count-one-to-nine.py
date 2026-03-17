import sys

input = sys.stdin.readline

# 선언부
def solve(n: int, n_list: list[int]):
    frequency_list = [0 for _ in range(9)]

    for i in range(n):
        frequency_list[n_list[i] - 1] += 1

    print(*frequency_list, sep='\n')

# 구현부
N = int(input())
number_list = list(map(int, input().split()))
solve(N, number_list)
