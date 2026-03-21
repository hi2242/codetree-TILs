import sys

input = sys.stdin.readline

# 선언부

# 구현부
A, B = input().rstrip().split()
print(int(A + B) + int(B + A))
