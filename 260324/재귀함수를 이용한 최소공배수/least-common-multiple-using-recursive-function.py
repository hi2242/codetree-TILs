import sys

input = sys.stdin.readline

# 선언부
def solve1(a: int, b: int):
    temp = 1
    for i in range(min(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            temp = i
            break
    return (a * b) // temp

def solve(n: int, n_list: list[int]):
    if n == 0:
        return n_list[0]
    m = solve(n - 1, n_list)
    return solve1(m, n_list[n])

# 구현부
n = int(input())
number_list = list(map(int, input().split()))
print(solve(n - 1, number_list))
