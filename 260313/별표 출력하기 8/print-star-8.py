import sys

input = sys.stdin.readline

# 선언부
def print_star(n: int):
    for i in range(1, n + 1):
        if i % 2 != 0:
            print('*', end='')
        else:
            for _ in range(i):
                print('*', end=' ')
        print()

# 입력부
N = int(input())

# 호출부
print_star(N)
