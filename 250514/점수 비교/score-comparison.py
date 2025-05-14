A = list(map(int, input().split()))
B = list(map(int, input().split()))

print((lambda x, y : 1 if x[0] > y[0] and x[1] > y[1] else 0)(A, B))