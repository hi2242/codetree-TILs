import sys

input = sys.stdin.readline

# 선언부
def solve(first: int, second: int):
    n_list = []
    n_list.append(first)
    n_list.append(second)

    for i in range(2, 10):
        n_list.append((n_list[i - 2] + n_list[i - 1]) % 10)

    print(*n_list)

# 구현부
first, second = map(int, input().split())
solve(first, second)
