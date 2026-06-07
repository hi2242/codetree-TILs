import sys

input = sys.stdin.readline

# 선언부
def solve():
    acc, count = 0, 0
    for i in range(N):
        acc += count
        if A[i] > B[i]:
            count += A[i] - B[i]
        else:
            count -= B[i] - A[i]
    print(acc)

# 구현부
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
solve()
