import sys

input = sys.stdin.readline

# 선언부
def solve():
    result = 0
    for i in range(C // A + 1):
        for j in range(C // B + 1):
            temp = A * i + B * j
            if temp <= C:
                result = max(result, temp)
    print(result)
    
# 구현부
A, B, C = map(int, input().split())
solve()
