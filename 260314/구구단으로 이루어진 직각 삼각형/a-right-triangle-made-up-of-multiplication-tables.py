import sys

input = sys.stdin.readline

# 선언부
def print_table(n: int):
    for i in range(1, n + 1):
        for j in range(1, n - i + 2):
            print(f'{i} * {j} = {i * j}', end='')
            if j != n - i + 1:
                print(' / ', end='')
        print()

# 입력부
N = int(input())

# 호출부
print_table(N)
