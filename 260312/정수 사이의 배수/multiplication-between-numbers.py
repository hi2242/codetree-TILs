import sys

input = sys.stdin.readline

# 선언부

# 정의부
A, B = map(int, input().split())

# 호출부
acc, count = 0, 0
for i in range(A, B + 1):
    if i % 5 == 0 or i % 7 == 0:
        acc += i
        count += 1

print(f'{acc} {acc / count:.1f}')