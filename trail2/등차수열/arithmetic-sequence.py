import sys

input = sys.stdin.readline

# 선언부
def solve():
    result = 0
    numbers.sort()
    for k in range(numbers[0] + 1, numbers[-1]):
        temp = 0
        for i in range(N):
            for j in range(i + 1, N):
                if k - numbers[i] == numbers[j] - k:
                    temp += 1
        result = max(result, temp)
    print(result)
                
# 구현부
N = int(input())
numbers = list(map(int, input().split()))
solve()
