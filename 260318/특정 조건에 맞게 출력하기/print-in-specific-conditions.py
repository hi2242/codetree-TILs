import sys

input = sys.stdin.readline

# 선언부
def solve(n_list: list[int]):
    for n in n_list:
        if n == 0:
            break
        if n % 2 == 0:
            print(n // 2, end=' ')
        else:
            print(n + 3, end=' ')

# 구현부
number_list = list(map(int, input().split()))
solve(number_list)
