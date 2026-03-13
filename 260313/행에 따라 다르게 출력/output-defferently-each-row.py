import sys

input = sys.stdin.readline

# 선언부
def print_number(n: int):
    temp = 1
    for i in range(1, n + 1):
        if i % 2 != 0:
            diff = 1
        else:
            diff = 2
        for _ in range(n):
            print(temp, end=' ')
            temp += diff
        print()
        
# 입력부
N = int(input())

# 출력부
print_number(N)
