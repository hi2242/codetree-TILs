import sys

input = sys.stdin.readline

# 선언부
def solve(N: str):
    result = 0
    for i in range(len(N)):
        result += int(N[i]) * (2 **(len(N) - i - 1))
    print(result)

# 구현부
N = input().rstrip()
solve(N)
