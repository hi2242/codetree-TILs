import sys

input = sys.stdin.readline

# 선언부
def solve(n_list: list[int]):
    odd_acc, even_acc = 0, 0
    for i in range(1, 11):
        if i % 2 == 0:
            even_acc += n_list[i - 1]
        else:
            odd_acc += n_list[i - 1]
    print(abs(odd_acc - even_acc))

# 구현부
number_list = list(map(int, input().split()))
solve(number_list)
