import sys

input = sys.stdin.readline

# 선언부
def decimal_to_binary(origin: int) -> str:
    result = ''
    temp = origin
    while True:
        result = str(temp % 2) + result
        temp //= 2
        if temp == 0:
            break
    return result

def binary_to_decimal(origin: str) -> int:
    result = 0
    n = len(origin)
    for i in range(n):
        result += int(origin[i]) * (2 ** (n - i - 1))
    return result

def solve(origin: str) -> None:
    temp = binary_to_decimal(origin) * 17
    print(decimal_to_binary(temp))

# 구현부
N = input().rstrip()
solve(N)
