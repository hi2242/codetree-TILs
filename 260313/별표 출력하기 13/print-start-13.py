import sys

input = sys.stdin.readline

# 선언부
def print_star(n: int):
    for i in range(1, 2 * n + 1):
        if i % 2 != 0:
            for _ in range(n - (i // 2)):
                print('*', end=' ')
        else:
            for _ in range(i // 2):
                print('*', end=' ')
        print()

# 호출부
N = int(input())

# 입력부
print_star(N)
