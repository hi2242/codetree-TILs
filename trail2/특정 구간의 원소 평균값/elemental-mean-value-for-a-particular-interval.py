import sys

input = sys.stdin.readline

# 선언부
def solve():
    result = 0
    for i in range(N):
        for j in range(i, N):
            temp = 0
            for k in range(i, j + 1):
                temp += numbers[k]
            avg = temp / (j - i + 1)
            for k in range(i, j + 1):
                if numbers[k] == avg:
                    result += 1
                    break
    print(result)

# 구현부
N = int(input())
numbers = list(map(int, input().split()))
solve()
