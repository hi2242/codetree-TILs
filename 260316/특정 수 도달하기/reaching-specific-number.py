import sys

input = sys.stdin.readline

# 선언부
def solve(n_list: list[int]):
    acc = 0
    for i in range(10):
        if n_list[i] >= 250:
            print(f'{acc} {acc / i:.1f}')
            break
        acc += n_list[i]
    else:
        print(f'{acc} {acc / 10:.1f}')

# 구현부
number_list = list(map(int, input().split()))
solve(number_list)
