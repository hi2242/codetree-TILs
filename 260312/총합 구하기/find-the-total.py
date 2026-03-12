import sys

input = sys.stdin.readline

# 선언부

# 입력부
A, B = map(int, input().split())

# 호출부
acc = 0
for i in range(A, B + 1):
    if i % 6 == 0 and i % 8 != 0:
        acc += i

print(acc)