import sys

input = sys.stdin.readline

# 선언부
def print_alphabet(n: int):
    temp = 65
    for _ in range(n):
        for _ in range(n):
            print(chr(temp), end='')
            temp += 1
        print()

# 입력부
N = int(input())

# 호출부
print_alphabet(N)
