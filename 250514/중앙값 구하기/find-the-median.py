A, B, C = map(int, input().split())

print((lambda a, b, c : a if b <= a <= c or c <= a <= b else b if a <= b <= c or c <= b <= a else c)(A, B, C))