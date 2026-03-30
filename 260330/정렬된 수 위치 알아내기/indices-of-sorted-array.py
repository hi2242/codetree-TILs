n = int(input())
sequence = list(map(int, input().split()))

arr = []

for i in range(n):
    arr.append((sequence[i], i))

arr.sort(key = lambda x: x[0])

ans = [0] * n

for i in range(n):
    orign_idx = arr[i][1]
    
    ans[orign_idx] = i + 1

for i in ans:
    print(i, end=" ")
