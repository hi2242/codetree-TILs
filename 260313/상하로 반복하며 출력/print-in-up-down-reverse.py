import sys

input = sys.stdin.readline

# 선언부
def print_number(n: int):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if j % 2 != 0:
                print(i, end='')
            else:
                print(n - i + 1, end='')
        print()

# 입력부
N = int(input())

# 호출부
print_number(N)
