import sys

input = sys.stdin.readline

# 선언부

# 입력부
n = int(input())

# 호출부
# count: [교실, 복도, 화장실]
count = [0, 0, 0]

for i in range(1, n + 1):
    if i % 12 == 0:
        count[2] += 1
    elif i % 3 == 0:
        count[1] += 1
    elif i % 2 == 0:
        count[0] += 1

print(*count)