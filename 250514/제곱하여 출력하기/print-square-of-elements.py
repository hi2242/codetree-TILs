N = int(input())

arr = list(map(int, input().split()))
temp = []

for elem in arr:
    temp.append(elem ** 2)

print(*temp)