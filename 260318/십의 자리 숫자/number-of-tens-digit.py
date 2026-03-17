import sys

input = sys.stdin.readline

# 선언부
def solve(n_list: list[int]):
    frequency_list = [0 for _ in range(10)]
    for n in n_list:
        if n == 0:
            break
        if n < 10:
            continue
        frequency_list[n // 10] += 1
    
    for i in range(1, 10):
        print(f'{i} - {frequency_list[i]}')

# 호출부
number_list = list(map(int, input().split()))
solve(number_list)
