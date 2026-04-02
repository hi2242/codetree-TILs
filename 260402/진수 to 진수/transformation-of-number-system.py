import sys

input = sys.stdin.readline

# 선언부
def A_to_decimal(A: int, N: str) -> int:
    result = 0
    n = len(N)
    for i in range(n):
        result += int(N[i]) * (A ** (n - i - 1))
    return result

def decimal_to_B(B: int, N: int) -> str:
    result = ''
    temp = N
    while True:
        result = str(temp % B) + result
        temp //= B
        if temp == 0:
            break
    return result

def solve(A: int, B: int, N: str) -> None:
    temp = A_to_decimal(A, N)
    print(decimal_to_B(B, temp))

# 구현부
A, B = map(int, input().split())
N = input().rstrip()
solve(A, B, N)
