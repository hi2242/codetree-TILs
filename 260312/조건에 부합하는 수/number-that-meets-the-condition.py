import sys

input = sys.stdin.readline

# 선언부

# 입력부
A = int(input())

# 호출부
for i in range(1, A + 1):
    if i % 2 == 0 and i % 4 != 0:
        continue
    elif (i // 8) % 2 == 0:
        continue
    elif i % 7 < 4:
        continue
    print(i, end=' ')