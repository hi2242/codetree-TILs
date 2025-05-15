N = int(input())

print(*["A" if i >= 90 else "B" if i >= 80 else "C" if i >= 70 else "D" if i >= 60 else "F" for i in range(N, 101)])