import sys

input = sys.stdin.readline

# 선언부
def solve():
    result = 0
    for i in range(M):
        start_i, end_i = min(numbers[i]), max(numbers[i])
        temp = 1
        for j in range(i + 1, M):
            start_j, end_j = min(numbers[j]), max(numbers[j])
            if start_i == start_j and end_i == end_j:
                temp += 1
        result = max(result, temp)
    print(result)

# 구현부
N, M = map(int, input().split())
numbers = [tuple(map(int, input().split())) for _ in range(M)]
solve()
