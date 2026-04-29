import sys

input = sys.stdin.readline

# 선언부
def solve():
    count = 0
    N = len(A)
    for i in range(N):
        if A[i] == '(':
            for j in range(i + 1, N):
                if A[j] == ')':
                    count += 1
    print(count)
    
# 구현부
A = input().rstrip()
solve()
