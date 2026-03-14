import sys

input = sys.stdin.readline

# 구현부
def print_number(n: int):
    temp = 1
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i <= j:
                print(temp, end=' ')
                temp += 1
                if temp > 9:
                    temp = 1
            else:
                print(' ', end=' ')
        print()

# 입력부
N = int(input())

# 출력부
print_number(N)
