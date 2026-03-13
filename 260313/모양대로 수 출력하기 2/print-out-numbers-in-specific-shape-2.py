import sys

input = sys.stdin.readline

# 선언부
def print_number(n: int):
    temp = 2
    for _ in range(n):
        for _ in range(n):
            print(temp, end=' ')
            temp += 2
            if temp > 8:
                temp = 2
        print()
        
# 입력부
N = int(input())

# 호출부
print_number(N)
