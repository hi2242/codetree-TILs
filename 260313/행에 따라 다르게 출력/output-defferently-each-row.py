import sys

input = sys.stdin.readline

# 선언부
def print_number(n: int):
    temp = 0
    for i in range(1, n + 1):
        if i % 2 != 0:
            diff = 1
        else:
            diff = 2
        for _ in range(n):
            temp += diff
            print(temp, end=' ')
        print()
        
# 입력부
N = int(input())

# 출력부
print_number(N)
