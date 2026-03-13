import sys

input = sys.stdin.readline

# 선언부
def print_number(n: int):
    for _ in range(n):
        for i in range(n, 0, -1):
            print(i, end=' ')
        print()
# 입력부
N = int(input())

# 호출부
print_number(N)
