import sys

input = sys.stdin.readline

# 선언부
def solve(n: int):
    n_list = [1, n]
    index = 2
    while True:
        n_list.append(n_list[index - 2] + n_list[index - 1])
        index += 1
        if n_list[index - 1] > 100:
            print(*n_list)
            break

# 구현부
N = int(input())
solve(N)
