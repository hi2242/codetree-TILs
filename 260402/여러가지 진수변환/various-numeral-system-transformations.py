import sys

input = sys.stdin.readline

# 선언부
def solve(N: int, B: int):
    result = ''
    temp = N
    while True:
        result = str(temp % B) + result
        temp //= B
        if temp == 0:
            break

    print(result)
    
# 구현부
N, B = map(int, input().split())
solve(N, B)
