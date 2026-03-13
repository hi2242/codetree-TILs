import sys

input = sys.stdin.readline

# 선언부
def print_number(n: int):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i >= j:
                print(i, end=' ')
        print()

# 입력부
N = int(input())

# 호출부
print_number(N)
