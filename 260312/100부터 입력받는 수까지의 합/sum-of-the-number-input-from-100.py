import sys

input = sys.stdin.readline

# 선언부

# 입력부
N = int(input())

# 호출부
acc = 0

for i in range(N, 101):
    acc += i

print(acc)