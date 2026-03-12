import sys

input = sys.stdin.readline

# 선언부

# 입력부
N = int(input())

# 호출부
acc = 0
for i in range(1, 101):
    acc += i
    if acc >= N:
        print(i)
        break