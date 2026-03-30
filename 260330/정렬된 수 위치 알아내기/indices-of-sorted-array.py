import sys

input = sys.stdin.readline

# 선언부
def solve(n: int, n_list: list[int]):
    temp = sorted(n_list)
    result = [0 for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not result[j] and temp[i] == n_list[j]:
                result[j] = i + 1
                break
    print(*result)

# 구현부
N = int(input())
n_list = list(map(int, input().split()))
solve(N, n_list)
