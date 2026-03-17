import sys

input = sys.stdin.readline

# 선언부
def solve(n: int, m: int, n_list: list[int]):
    count = 0
    for i in range(n):
        if n_list[i] == m:
            count += 1
    print(count)
    
# 구현부
N, M = map(int, input().split())
number_list = list(map(int, input().split()))
solve(N, M, number_list)
