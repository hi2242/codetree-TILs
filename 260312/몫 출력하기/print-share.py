import sys

input = sys.stdin.readline

# 선언부

# 입력부

# 호출부
count = 0
while True:
    i = int(input())
    if i % 2 != 0:
        continue
    else:
        print(i // 2)
        count += 1

    if count == 3:
        break