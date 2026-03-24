import sys

input = sys.stdin.readline

# 선언부
def solve(n: int, n_list: list[int]):
    if n == 0:
        return n_list[0]
    m = solve(n - 1, n_list)
    maximum, minimum = max(m, n_list[n]), min(m, n_list[n])
    temp = 1
    for i in range(minimum, 0, -1):
        if maximum % i == 0 and minimum % i == 0:
            temp = i
            break
    return maximum if maximum % minimum == 0 else (m * n_list[n]) // temp

# 구현부
n = int(input())
number_list = list(map(int, input().split()))
print(solve(n - 1, number_list))
