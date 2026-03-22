import sys

input = sys.stdin.readline

# 선언부
def solve(n: int):
    acc = 0
    for i in range(1, n + 1):
        acc += i
    print(acc // 10)
    
# 구현부
N = int(input())
solve(N)
