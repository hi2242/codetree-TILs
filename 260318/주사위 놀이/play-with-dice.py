import sys

input = sys.stdin.readline

# 선언부
def solve(n_list: list[int]):
    frequency_list = [0 for _ in range(6)]
    for n in n_list:
        frequency_list[n - 1] += 1
    
    for i in range(6):
        print(f'{i + 1} - {frequency_list[i]}')

# 구현부
number_list = list(map(int, input().split()))
solve(number_list)
