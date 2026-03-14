import sys

input = sys.stdin.readline

# 구현부
def print_pyramid(n: int):
    temp = 1
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i >= j:
                print(temp, end=' ')
                temp += 1
            else:
                print(' ', end=' ')
        print()

# 입력부
N = int(input())

# 호출부
print_pyramid(N)
