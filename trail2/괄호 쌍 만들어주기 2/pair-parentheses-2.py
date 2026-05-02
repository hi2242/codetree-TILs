import sys

input = sys.stdin.readline

# 선언부
def solve():
    A_length = len(A)
    result = 0
    for i in range(1, A_length):
        if A[i - 1] == '(' and A[i] == '(':
            for j in range(i + 2, A_length):
                if A[j - 1] == ')' and A[j] == ')':
                    result += 1
    print(result)
    
# 구현부
A = input().rstrip()
solve()
