import sys

input = sys.stdin.readline

# 선언부

# 입력부
N = int(input())

# 호출부
prod = 1
for i in range(1, 11):
    prod *= i
    if prod >= N:
        print(i)
        break