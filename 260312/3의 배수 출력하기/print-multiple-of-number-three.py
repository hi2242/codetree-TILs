import sys

input = sys.stdin.readline

# 선언부

# 입력부
N = int(input())

# 호출부
temp = 3

while temp <= N:
    print(temp, end=' ')
    temp += 3