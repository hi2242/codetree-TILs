import sys

input = sys.stdin.readline

# 선언부
def solve():
    cow_count = len(A)
    result = 0
    for i in range(cow_count):
        for j in range(i + 1, cow_count):
            for k in range(j + 1, cow_count):
                if A[i] <= A[j] <= A[k]:
                    result += 1
    print(result)
    
# 구현부
N = int(input())
A = list(map(int, input().split()))
solve()
