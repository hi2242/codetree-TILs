import sys

input = sys.stdin.readline

# 선언부

# 구현부
N = int(input())
max_count, count = 1, 1
for i in range(N):
    temp = int(input())
    
    if i == 0:
        preview = temp
        continue
    if temp > preview:
        count += 1
        max_count = max(max_count, count)
    else:
        count = 1
    preview = temp

print(max_count)
