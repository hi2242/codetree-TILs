import sys

input = sys.stdin.readline

# 선언부
def solve():
    result = [0 for _ in range(N)]
    for i in range(1, N + 1):
        result[0] = i
        for j in range(N - 1):
            if not (1 <= A_sums[j] - result[j] <= N) or A_sums[j] - result[j] in result:
                result = [0 for _ in range(N)]
                break
            result[j + 1] = A_sums[j] - result[j]
        else:
            print(*result)
            break

# 구현부
N = int(input())
A_sums = list(map(int, input().split()))
solve()
