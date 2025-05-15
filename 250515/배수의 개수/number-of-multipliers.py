arr = list(int(input()) for _ in range(10))

print(len([i for i in arr if i % 3 == 0]), len([i for i in arr if i % 5 == 0]))