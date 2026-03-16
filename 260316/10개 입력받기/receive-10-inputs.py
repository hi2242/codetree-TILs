import sys

input = sys.stdin.readline

# 선언부
def solve(n_list: list[int]):
    acc, count = 0, 0
    for n in n_list:
        if n == 0:
            break
        acc += n
        count += 1
    print(f'{acc} {acc / count:.1f}')
    
# 구현부
number_list = list(map(int, input().split()))
solve(number_list)
