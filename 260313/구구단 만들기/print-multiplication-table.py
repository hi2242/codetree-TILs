import sys

input = sys.stdin.readline

# 선언부
def print_table(start: int, end: int):
    for i in range(1, 10):
        for j in range(start, end - 1, -2):
            print(f'{j} * {i} = {j * i}', end='')
            if j != end:
                print(' / ', end='')
        print()

# 입력부
A, B = map(int, input().split())

# 호출부
print_table(B, A)