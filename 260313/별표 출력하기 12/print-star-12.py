import sys

input = sys.stdin.readline

# 선언부
def calculate_row(n: int):
    if n == 1 or n % 2 == 0:
        return n
    else:
        return n - 1
    
def print_star(n: int):
    row = calculate_row(n)

    for i in range(1, row + 1):
        for j in range(1, n + 1):
            if i == 1:
                print('*', end=' ')
            else:
                if j <= i - 1 or j % 2 != 0:
                    print(' ', end=' ')
                else:
                    print('*', end=' ')
        print()


# 입력부
N = int(input())

# 호출부
print_star(N)
