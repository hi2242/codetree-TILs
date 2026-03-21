import sys

input = sys.stdin.readline

# 선언부

# 구현부
N = int(input())
acc = 0
for _ in range(N):
    temp = int(input())
    acc += temp
acc = str(acc)
print(acc[1:] + acc[0])
