import sys

input = sys.stdin.readline

# 선언부
def check_even(n: int):
    return (n // 10 + n % 10) % 2 == 0
    
def solve(start: int, end: int):
    count = 0
    for i in range(start, end + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            if check_even(i):
                count += 1
    print(count)

# 구현부
A, B = map(int, input().split())
solve(A, B)
