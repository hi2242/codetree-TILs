import sys

input = sys.stdin.readline

# 선언부
def solve(n: int, n_list: list[int]):
    temp = []
    for i in range(n):
        temp.append(n_list[i])
    temp.sort()
    print(temp[n // 2], end=' ')

# 구현부
N = int(input())
n_list = list(map(int, input().split()))
for i in range(1, N + 1):
    if i % 2 != 0:
        solve(i, n_list)
