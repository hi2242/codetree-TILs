import sys

input = sys.stdin.readline

# 선언부
def solve(n_list: list[int]):
    temp_list = []
    for n in n_list:
        if n == 0:
            break
        temp_list.append(n)

    temp_list.reverse()
    print(*temp_list)

# 구현부
number_list = list(map(int, input().split()))
solve(number_list)
