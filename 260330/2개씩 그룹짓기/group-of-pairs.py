import sys

input = sys.stdin.readline

# 선언부
def solve(n: int, n_list: list[int]):
    sorted_list = sorted(n_list)
    t_list = []
    for i in range(2 * n):
        t_list.append(sorted_list[i] + sorted_list[2 * n - i - 1])
    print(max(t_list))

# 구현부
N = int(input())
n_list = list(map(int, input().split()))
solve(N, n_list)
