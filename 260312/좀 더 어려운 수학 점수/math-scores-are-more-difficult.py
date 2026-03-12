import sys

input = sys.stdin.readline

A = list(map(int, input().split()))
B = list(map(int, input().split()))

def program():
    if A[0] > B[0]:
        return 'A'
    elif B[0] > A[0]:
        return 'B'
    else:
        if A[1] > B[1]:
            return 'A'
        elif B[1] > A[1]:
            return 'B'
    
print(program())