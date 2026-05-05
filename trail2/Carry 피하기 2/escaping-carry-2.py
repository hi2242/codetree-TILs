import sys

input = sys.stdin.readline

# 선언부
def calc(n: int, l: int):
    return n // (10 ** l) % 10
    
def adder(a: int, b: int):
    min_length_ab = min(len(str(a)), len(str(b)))
    for i in range(min_length_ab):
        if calc(a, i) + calc(b, i) >= 10:
            return -1
    else:
        return a + b

def solve():
    result = -1
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            for k in range(j + 1, N):
                temp = adder(numbers[i], numbers[j])
                if temp:
                    result = max(result, adder(temp, numbers[k]))
    print(result)

# 구현부
N = int(input())
numbers = []
for _ in range(N):
    numbers.append(int(input()))
solve()
