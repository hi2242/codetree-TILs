import sys

input = sys.stdin.readline

# 선언부
def solve(n_list: list[int]):
    print(n_list[2] + n_list[4] + n_list[9])
    
# 구현부
number_list = list(map(int, input().split()))
solve(number_list)
