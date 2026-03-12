import sys

input = sys.stdin.readline

# 선언부

# 입력부
N, a = map(int, input().split())

# 호출부
temp = 1
while temp <= N:
    if temp % a == 0:
        print(1)
    else:
        print(0)

    temp += 1