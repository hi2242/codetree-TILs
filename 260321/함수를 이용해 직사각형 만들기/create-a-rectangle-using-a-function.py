import sys

input = sys.stdin.readline

# 선언부
def solve(n: int, m: int):
    for _ in range(n):
        for _ in range(m):
            print(1, end='')
        print()
        
# 구현부
n, m = map(int, input().split())
solve(n, m)
