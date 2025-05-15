N = int(input())

arr = list(map(int, input().split()))

print(*reversed([i for i in arr if i % 2 == 0]))