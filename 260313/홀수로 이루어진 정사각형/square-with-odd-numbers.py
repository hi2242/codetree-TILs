import sys

input = sys.stdin.readline

# 선언부
def print_number(n: int):
    for i in range(1, n * 2 + 1, 2):
        for j in range(i, n * 2 + i, 2):
            print(10 + j, end=' ')
        print()

# 입력부
N = int(input())

# 호출부
print_number(N)
