import sys

input = sys.stdin.readline

# 선언부
def solve(n: int, n_list: list[int]):
    new_n_list = []
    for n in n_list:
        if n % 2 == 0:
            new_n_list.append(n)

    print(*new_n_list)
    
# 구현부
N = int(input())
number_list = list(map(int, input().split()))
solve(N, number_list)
