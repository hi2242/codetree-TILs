arr = list(map(int, input().split()))

for _ in range(8):
    arr.append((arr[-1] + arr[-2]) % 10)

print(*arr)