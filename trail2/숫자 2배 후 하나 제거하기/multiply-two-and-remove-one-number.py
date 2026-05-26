import sys

input = sys.stdin.readline

INF = float('inf')
# 선언부
def solve():
    result = INF
    for i in range(N):
        numbers[i] *= 2
        for j in range(N):
            temp = 0
            temp_arr = []
            for k in range(N):
                if j == k:
                    continue
                temp_arr.append(numbers[k])
            for k in range(N - 2):
                temp += abs(temp_arr[k] - temp_arr[k + 1])
            result = min(result, temp)
        numbers[i] //= 2
    print(result)

# 구현부
N = int(input())
numbers = list(map(int, input().split()))
solve()
