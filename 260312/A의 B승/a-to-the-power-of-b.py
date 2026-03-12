import sys

input = sys.stdin.readline

# 선언부

# 입력부
A, B = map(int, input().split())

# 호출부
acc = 1

for i in range(B):
    acc *= A

print(acc)