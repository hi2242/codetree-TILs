import sys

input = sys.stdin.readline

# 선언부
def solve():
    sum_of_numbers = sum(numbers)
    diff = int(1e9)
    for i in range(N - 1):
        for j in range(i + 1, N):
            diff = min(diff, abs(S - (sum_of_numbers - numbers[i] - numbers[j])))
    print(diff)

# 구현부
N, S = map(int, input().split())
numbers = list(map(int, input().split()))
solve()
