import sys

input = sys.stdin.readline

# 선언부
def solve():
    result = 0
    for i in range(N - M + 1):
        temp = A[i : i + M]
        temp.sort()
        for j in range(M):
            if temp[j] != B[j]:
                break
        else:
            result += 1
    print(result)

# 구현부
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
B.sort()
solve()
