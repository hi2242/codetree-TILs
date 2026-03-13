import sys

input = sys.stdin.readline

# 선언부
def print_number(n: int):
    temp = 1
    for _ in range(n):
        for _ in range(n):
            print(temp, end=' ')
            temp += 1
        print()

# 입력부
N = int(input())

# 호출부
print_number(N)
