import sys

input = sys.stdin.readline

# 선언부
def print_table():
    for i in range(1, 20):
        for j in range(1, 20):
            print(f'{i} * {j} = {i * j}', end='')
            if j == 19 or j % 2 == 0:
                print()
            else:
                print(' / ', end='')

# 입력부

# 호출부
print_table()
