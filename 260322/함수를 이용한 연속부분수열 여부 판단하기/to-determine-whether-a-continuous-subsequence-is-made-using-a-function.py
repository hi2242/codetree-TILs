import sys

input = sys.stdin.readline

# 선언부
def solve(n1: int, n2: int, A: list[int], B: list[int]):
    for i in range(n1 - n2 + 1):
        if A[i] == B[0]:
            for j in range(n2):
                if A[i + j] != B[j]:
                    break
            else:
                print('Yes')
                return
    else:
        print('No')

# 구현부
n1, n2 = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
solve(n1, n2, A, B)
