import sys

input = sys.stdin.readline

# 선언부
def print_number(r: int, c: int):
    for i in range(1, r + 1):
        for j in range(i, i * c + 1, i):
            print(j, end=' ')
        print()

# 입력부
A, B = map(int, input().split())

# 호출부
print_number(A, B)