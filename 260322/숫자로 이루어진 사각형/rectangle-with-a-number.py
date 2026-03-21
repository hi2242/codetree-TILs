import sys

input = sys.stdin.readline

# 선언부
def solve(n: int):
    temp = 1
    for _ in range(n):
        for _ in range(n):
            print(temp, end=' ')
            temp += 1
            if temp == 10:
                temp = 1
        print()
        
# 구현부
N = int(input())
solve(N)
