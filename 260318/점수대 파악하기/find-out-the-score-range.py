import sys

input = sys.stdin.readline

# 선언부
def solve(n_list: list[int]):
    range_list = [0 for _ in range(11)]
    for n in n_list:
        if n == 0:
            break
        range_list[n // 10] += 1
    for i in range(10, 0, -1):
        print(f'{i * 10} - {range_list[i]}')
        
# 구현부
number_list = list(map(int, input().split()))
solve(number_list)
