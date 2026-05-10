import sys

input = sys.stdin.readline

# 선언부
def check(r: int, c: int) -> int:
    result = 0
    for i in range(3):
        result += grid[r][c + i]
    return result

def solve():
    result = 0
    for first_r in range(N):
        for first_c in range(N - 2):
            for second_r in range(first_r, N):
                for second_c in range(N - 2):
                    if second_r == first_r and first_c - 2 <= second_c <= first_c + 2:
                        continue
                    result = max(result, check(first_r, first_c) + check(second_r, second_c))
    print(result)

# 구현부
N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
solve()
