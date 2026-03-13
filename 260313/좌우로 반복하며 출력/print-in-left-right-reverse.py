import sys

input = sys.stdin.readline

# 선언부
def print_number(n: int):
    for i in range(1, n + 1):
        if i % 2 != 0:
            temp, diff = 1, 1
        else:
            temp, diff = n, -1
        for _ in range(n):
            print(temp, end='')
            temp += diff
        print()
                
# 입력부
N = int(input())

# 호출부
print_number(N)
