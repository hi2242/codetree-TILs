import sys

input = sys.stdin.readline

# 선언부
def solve(n_list: list[int]):
    even_acc = 0
    third_acc, third_count = 0, 0
    for i in range(10):
        if (i + 1) % 2 == 0:
            even_acc += n_list[i]
        if (i + 1) % 3 == 0:
            third_acc += n_list[i]
            third_count += 1
    print(f'{even_acc} {third_acc / third_count:.1f}')

# 구현부
number_list = list(map(int, input().split()))
solve(number_list)
