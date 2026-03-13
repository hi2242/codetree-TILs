import sys

input = sys.stdin.readline

# 선언부
def print_star(n: int):
    for i in range(1, 2 * n + 2):
        for j in range(1, 2 * n + 2):
            if i % 2 == 0 and j % 2 == 0:
                print(' ', end=' ')
                continue
            print('*', end=' ')
        print()

# 입력부
N = int(input())

# 호출부
print_star(N)
