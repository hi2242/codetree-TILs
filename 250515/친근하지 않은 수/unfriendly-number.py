N = int(input())

print(len([i for i in range(1, N + 1) if i % 2 != 0 and i % 3 != 0 and i % 5 != 0]))