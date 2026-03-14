import sys

input = sys.stdin.readline

# 선언부
def print_alphabet(n: int):
    temp = 65
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i <= j:
                print(chr(temp), end=' ')
                temp += 1
                if temp > 90:
                    temp = 65
            else:
                print(' ', end=' ')
        print()

# 입력부
N = int(input())

# 호출부
print_alphabet(N)
