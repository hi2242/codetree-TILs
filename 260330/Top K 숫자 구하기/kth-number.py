import sys

input = sys.stdin.readline

# 선언부
def solve(n: int, k: int, n_list: list[int]):
    temp = sorted(n_list)
    print(temp[k - 1])
    
# 구현부
N, K = map(int, input().split())
n_list = list(map(int, input().split()))
solve(N, K, n_list)
